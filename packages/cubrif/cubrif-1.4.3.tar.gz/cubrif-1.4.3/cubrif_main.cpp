#include "brif.h"
#if defined(__linux__) || defined(__APPLE__)
#include <sys/time.h>
double cpuSecond(){
    struct timeval tp;
    gettimeofday(&tp, NULL);
    return((double)tp.tv_sec + (double)tp.tv_usec*1.e-6);
}
#else
double cpuSecond(){
    return((double)clock()/CLOCKS_PER_SEC);
}
#endif


int main(int argc, char* argv[]){
    
    if(argc != 2){
        puts("Build Random Forest with CUDA acceleration.");
        printf("Usage: %s config.txt\n", argv[0]);
        puts("The config.txt file should contain parameter name and value pairs separated by space, one pair per line.");
        puts("Lines starting with # will be ignored.");
        puts("Parameters:");
        puts("trainfile | Required | training data filename string (no quote, no space)");
        puts("n         | Required | number of rows in training data");
        puts("p         | Required | number of variables in training data (not counting the first column which is the target variable)");
        puts("validfile | Optional | test data filename string (no quote, no space)");
        puts("outfile   | Optional | filename for where to write scoring output, if missing, write on stdout");
        puts("valid_n   | Optional | number of rows in test data (required if validfile is given)");
        puts("Other parameters and their default values (and notes):");
        puts("valid_X_only 0 (0 means valid data has y as first column; 1 means X matrix only)");
        puts("min_node_size 1");
        puts("max_depth 20");
        puts("max_integer_classes 10");
        puts("n_numeric_cuts 31");
        puts("n_integer_cuts 31");
        puts("ntrees 1 (number of trees in the forest)");
        puts("blocksize 64 (thread block size for CUDA)");
        puts("n_lb_GPU 20480 (n must be above this value to use GPU when GPU = 2 (hybrid mode)");
        puts("nthreads 1 (number of threads for OpenMP)");
        puts("GPU 0 (0 for CPU only, 1 for CPU + GPU)");
        exit(1);
    } 

    FILE *fp = fopen(argv[1], "r");
    if(fp == NULL){
        printf("Cannot open file %s\n", argv[1]);
        exit(1);
    }

    // Global configuration variables
    int n = 0;  // number of rows in training set
    int p = 0;  // number of predictors
    int GPU = 0; // 0: CPU, 1: GPU
    char trainfile[200] = {'\0'};  // training data file name
    char validfile[200] = {'\0'};  // validation data file name
    char outfile[200] = {'\0'};  // validation data file name
    int valid_n = 0;  // number of rows in validation file
    int valid_X_only = 0; 
    int min_node_size = 1;  // minimum node size
    int max_depth = 20; 
    int max_integer_classes = 10;
    int n_numeric_cuts = 31;
    int n_integer_cuts = 31;
    int ntrees = 1;
    int nthreads = 1;
    int blocksize = 128;
    int ubthresh = 640;  // for n = 32*64*10 = 20480 
    int seed = 2022;

    char linebuf[330];
    char key1[30], key2[100], remainder[200];
    while (fscanf(fp, "%[^\n] ", linebuf) != EOF){
        sscanf(linebuf, "%19s %99s %199[^\n]", key1, key2, remainder);
        if(strcmp(key1, "#") == 0) continue;  // # marks the comment line
        if(!strcmp(key1, "n")){
            n = atoi(key2);
        } else if(!strcmp(key1, "p")){
            p = atoi(key2);
        } else if(!strcmp(key1, "trainfile")){
            strcpy(trainfile, key2);
        } else if(!strcmp(key1, "valid_n")){
            valid_n = atoi(key2);
        } else if(!strcmp(key1, "valid_X_only")){
            valid_X_only = atoi(key2);
        } else if(!strcmp(key1, "validfile")){
            strcpy(validfile, key2);
        } else if(!strcmp(key1, "min_node_size")){
            min_node_size = atoi(key2);
        } else if(!strcmp(key1, "max_depth")){
            max_depth = MIN(MAXDEPTH,atoi(key2));
        } else if(!strcmp(key1, "ntrees")){
            ntrees = atoi(key2);
        } else if(!strcmp(key1, "nthreads")){
            nthreads = atoi(key2);
        } else if(!strcmp(key1, "seed")){
            seed = atoi(key2);
        } else if(!strcmp(key1, "blocksize")){
            blocksize = atoi(key2);
        } else if(!strcmp(key1, "outfile")){
            strcpy(outfile, key2);
        } else if(!strcmp(key1, "GPU")){
            GPU = atoi(key2);
        } else if(!strcmp(key1, "n_lb_GPU")){
            ubthresh = atoi(key2) / sizeof(bitblock_t);
        } else if(!strcmp(key1, "max_integer_classes")){
            max_integer_classes = atoi(key2);
        } else if(!strcmp(key1, "n_integer_cuts")){
            n_integer_cuts = atoi(key2);
        } else if(!strcmp(key1, "n_numeric_cuts")){
            n_numeric_cuts = atoi(key2);
        }
    }

    printf("n = %d, p = %d, ntrees = %d, nthreads = %d, GPU = %d, blocksize %d, n_lb_GPU %ld\n", n, p, ntrees, nthreads, GPU, blocksize, ubthresh*sizeof(bitblock_t));
    printf("min_node_size = %d, max_depth = %d\n", min_node_size, max_depth);
    printf("n_numeric_cuts = %d, n_integer_cuts = %d, max_integer_classes = %d, seed = %d\n", n_numeric_cuts, n_integer_cuts, max_integer_classes, seed);


    if(blocksize % 64){
        printf("Invalid blocksize. Must be a multiple of 64.\n");
        exit(1);
    }

    double begtime;
    rf_model_t *model = NULL;
    begtime = cpuSecond();
    //data_frame_t *train_df = get_data("tmp_brif_traindata.txt", &model, 416,7, 0);
    printf("Reading file %s\n", trainfile);
    data_frame_t *train_df = get_data(trainfile, &model, n, p, 0);
    if(train_df == NULL){
        printf("Error reading training data.\n");
        if(model != NULL) delete_model(model);
        exit(1);
    }
    printf("Finished reading data. Time elapsed: %0.5f\n",cpuSecond() - begtime);

    int ps = (int)(round(sqrt(model->p)));

    
    begtime = cpuSecond();
    make_cuts(train_df, &model, n_numeric_cuts, n_integer_cuts);   
    bx_info_t *bx_train = make_bx(train_df, &model, nthreads);
    ycode_t *yc_train = make_yc(train_df, &model, max_integer_classes, nthreads);
    delete_data(train_df); 
    printf("Finished making bx and yc using %d threads. Time elapsed: %0.5f\n", nthreads, cpuSecond() - begtime);
    begtime = cpuSecond();
    if(GPU == 0){
        printf("Using CPU to build forest ...\n");
        build_forest(bx_train, yc_train, &model, ps, max_depth, min_node_size, ntrees, nthreads, seed);
    } else if(GPU == 1) {
        printf("Using GPU to build forest ...\n");
        build_forest_cuda(bx_train, yc_train, &model, ps, max_depth, min_node_size, ntrees, nthreads, blocksize, seed);
    } else {
        printf("Using CPU + GPU hybrid mode to build forest ...\n");
        build_forest_hybrid(bx_train, yc_train, &model, ps, max_depth, min_node_size, ntrees, nthreads, blocksize, ubthresh, seed);        
    }
    
    printf("Build forest %d threads. Time elapsed: %0.5f\n", nthreads, cpuSecond() - begtime);

    delete_bx(bx_train, model);
    delete_yc(yc_train);


    flatten_model(&model, nthreads);

    //printRules(model, 0);  // print the first tree

    //data_frame_t *test_df = get_data("tmp_brif_testdata.txt", &model, 9,7, 1);
    printf("Reading file %s\n", validfile); 
    data_frame_t *test_df = get_data(validfile, &model, valid_n, p, valid_X_only);
    if(test_df == NULL){
        printf("Error reading test data.\n");
        if(model != NULL) delete_model(model);
        exit(1);
    }

    int test_n = test_df->n; 
    //print_data_summary(test_df);  
    bx_info_t *bx_test = make_bx(test_df, &model, nthreads);

    delete_data(test_df);

    FILE *outfileptr;
    if(strlen(outfile) == 0){
        outfileptr = stdout;
    } else {
        outfileptr = fopen(outfile,"w");
    }

    // prepare score matrix
    double **score = (double **)malloc(model->yc->nlevels*sizeof(double*));
    for(int k = 0; k < model->yc->nlevels; k++){
        score[k] = (double*)malloc(test_n*sizeof(double));
        memset(score[k], 0, test_n*sizeof(double));
    }
    predict(model, bx_test, score, 1, nthreads);
    delete_bx(bx_test, model);            
    
    // Write header line
    if(model->yc->type == CLASSIFICATION && model->yc->yvalues_num == NULL){
        for(int k = 0; k < model->yc->nlevels; k++){
            char var_name[MAX_VAR_NAME_LEN];
            if(model->yc->yvalues_int != NULL){
                if(model->var_types[0] == 'f'){  // if the target variable is a factor
                    int this_level_index = model->yc->yvalues_int[k] - model->yc->start_index;
                    fprintf(outfileptr, "%s ", model->yc->level_names[this_level_index]);
                } else {
                    fprintf(outfileptr, "%d ", model->yc->yvalues_int[k]);
                }
            }
        }
        fprintf(outfileptr, "\n");
    } else if(model->yc->type == REGRESSION || (model->yc->type == CLASSIFICATION && model->yc->yvalues_num != NULL)){
        fprintf(outfileptr, "pred\n"); 
    }

    // Write each value line
    double pred;
    if(model->yc->type == REGRESSION){
        for(int i = 0; i < test_n; i++){
            pred = 0;
            for(int k = 0; k < model->yc->nlevels; k++){
                pred += model->yc->yavg[k]*score[k][i];
            }
            fprintf(outfileptr, "%f \n", pred);
        }
    } else if(model->yc->type == CLASSIFICATION && model->yc->yvalues_num != NULL){
        for(int i = 0; i < test_n; i++){
            pred = 0;
            for(int k = 0; k < model->yc->nlevels; k++){
                pred += model->yc->yvalues_num[k]*score[k][i];
            }
            fprintf(outfileptr, "%f \n", pred);
        }  
    } else {
        for(int i = 0; i < test_n; i++){
            for(int k = 0; k < model->yc->nlevels; k++){
                fprintf(outfileptr, "%f ", score[k][i]);
            }
            fprintf(outfileptr, "\n");
        }
    }


    if(strlen(outfile) != 0){
        printf("Prediction results written to %s\n", outfile);
        fclose(outfileptr);
    }

    for(int k = 0; k < model->yc->nlevels; k++){
        free(score[k]);
    }
    free(score);

    delete_model(model);
    
    printf("All done.\n");
}
