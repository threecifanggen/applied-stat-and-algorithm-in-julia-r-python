library(ggplot2)

plot.surv_patient <- function(df, delete.status.col, survive.time.col, group) {
  df %>%
    with(ggplot(., aes(x=1:nrow(df), y=df[[as.name(survive.time.col)]])) +
      geom_point(aes(color=df[[group]]), shape=as.factor(df[[as.name(delete.status.col)]]), size=3) +
      geom_bar(aes(fill=df[[group]]),stat="identity", width=0.15) + 
      ylab("Surviver time") + 
      xlab("Subject") + 
      scale_fill_discrete(name = "Group") + 
      scale_color_discrete(name = "Group") + 
      scale_shape_discrete(name="Censoring") + 
      coord_flip())
}
