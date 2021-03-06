# BCC algorithm analysis with graph

library(basicTrendline)
library(spatialEco)

data=read.csv("./biconnectivity_tests/output.csv",sep="\t")

par(mfrow=c(2,2))
trendline(data$vertex,data$edge,model='line3P',
          main="F1 Polynomial y=a*x^2+b*x+c",
          xlab="vertex",ylab="edge",pch=20)
trendline(data$vertex+data$edge,data$time,model='line2P',
          main="F2 Linear y=a*x+b",
          xlab="vertex+edge",ylab="time",pch=20)
trendline(data$vertex,data$time,model='line2P',
          main="F3 Linear y=a*x+b",
          xlab="vertex",ylab="time",pch=20)
trendline(data$edge,data$time,model='line2P',
          main="F4 Linear y=a*x+b",
          xlab="edge",ylab="time",pch=20)

summary(data$vertex)
summary(data$edge)
summary(data$vertex+data$edge)