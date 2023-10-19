#!/usr/bin/env Rscript

library(Seurat)
chan_latest_030423 <- readRDS("~/Documents/School/phd/mini-projects/chans_data/labelled/chan_latest_030423.rds")


m_w = c('Wildtype','Mutant') ##the conditions we care about
cells_to_keep = c('IN1','IN2','DLN','IN Progenitor') ##the cells we want

for (value in cells_to_keep){
  for (cond in m_w){
    cat(paste0(cond,value))
    subset_seurat <- subset(chan_latest_030423,subset = condition == cond, idents = value)
    expression_matrix <- subset_seurat[["RNA"]]@counts
    expression_matrix <- as.matrix(expression_matrix)
    expression_df <- as.data.frame(expression_matrix)
    write.csv(expression_df, file = paste0("~/Documents/School/phd/mini-projects/chans_data/labelled/subset_",cond,"_",value,".csv"))
    
    
  }
}



