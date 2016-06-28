library(dplyr)
library(ggplot2)
library(survival)
library(readxl)

#setwd("~/Desktop/BUF_DataScience/2_tidydata_survival_analysis/whas500")
df <- read_excel("whas500.xls")

summary(df$lenfol)

dead <- df[df$fstat>0,]
ggplot(dead, aes(lenfol)) +
  geom_histogram(bins=20)


time_of_event <- df$lenfol
event <- df$fstat
time <- seq(0,2500,100)

srv <-Surv(time = time_of_event,event =event)

my.fit <- survfit(srv ~ 1)
plot(my.fit, main="Kaplan-Meier estimate with 95% confidence bounds", xlab="time", ylab="survival function")

#stratify Congestive Heart Complications
srv_w <-Surv(time = time_of_event[df$chf==1],event =event[df$chf==1])

srv_wo <-Surv(time = time_of_event[df$chf!=1],event =event[df$chf!=1])


new.srv <-Surv(time = time_of_event,event =event)

cph <- coxph( new.srv ~ (fstat + lenfol + bmi+ age),data=df)

