# CPP algorithm analysis with graph

library(basicTrendline)
library(spatialEco)

genGraph <- function(file){
  data=read.csv(file,sep="\t")
  data=data[order(data$num),]
  attach(data)
  
  par(mfrow=c(2,2))
  lm1<-lm(v1 ~ num + I(num**2))
  lm2<-lm(v2 ~ num+I(num*(log(num))))
  lm3<-lm(v3 ~ num+I(num*log(num)))
  print(lm1)
  print(lm2)
  print(lm3)
  
  trendline(num, v1, model='line3P',
            main="V1 n^2 y=a*x^2+b*x+c",
            xlab="number",ylab="time",pch=20)
  plot(num, v2, pch=20,xlab="number",ylab="time",
       main="V2 O(n(log(n))^2)")
  lines(num,lm2$fitted.values,col=2,lwd=2)
  plot(num, v3, pch=20,xlab="number",ylab="time",
       main="V3 O(nlog(n))")
  lines(num,lm3$fitted.values,col=2,lwd=2)

  par(mfrow=c(1,1))  
  plot(num, v2, pch = 20, col = "red", 
       xlab="number", ylab="time", 
       main="v2 vs v3 Comparison")
  legend("topleft", legend = c("v2", "v3"), 
         col=c("red", "cyan"), lwd = 3)
  points(num, v3, pch = 20, col="cyan")
  lines(num,lm2$fitted.values,col=2,lwd=2)
  lines(num,lm3$fitted.values,col="cyan",lwd=2)
  
  par(mfrow=c(1,1))
  
  trendline(num, v1, ePos.x = NA, model='line3P', 
            main="Overall Comparison",
            xlab="number", ylab="time",pch=20, 
            linecolor="black",lwd=5)
  
  legend("topleft", legend = c("v1", "v2", "v3"), 
         col=c("black", "red", "cyan"), lwd = 3)
  
  points(num, v2, pch = 20, col="red")
  points(num, v3, pch = 20, col="cyan")
  lines(num,lm2$fitted.values,col=2,lwd=15)
  lines(num,lm3$fitted.values,col="cyan",lwd=5)
  detach(data)
}

file1="/Users/linni/Documents/CSE417/HW4/outRand.csv"
genGraph(file1)

file2="/Users/linni/Documents/CSE417/HW4/outVer.csv"
genGraph(file2)
