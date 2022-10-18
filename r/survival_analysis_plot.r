library(ggplot2)

plot.surv_patient <- function(df, delete.status.col, survive.time.col) {
  ggplot(df, aes(x=1:nrow(df), y=survive.time.col)) + geom_point() + geom_bar(aes(fill=as.factor(group)),stat="identity", width=0.2) + coord_flip()
}
