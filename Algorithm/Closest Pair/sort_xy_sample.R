x<-c(0,1,2,2.1,2.2)
y<-c(2,-2,4,-10,4.1)
plot(x,y,pch=20,main="sort by x")
for (i in 1:4) {
  vx<-c(x[i],x[i+1])
  vy<-c(y[i],y[i+1])
  lines(vx,vy)
}
vx<-c(x[3],x[5])
vy<-c(y[3],y[5])
lines(vx,vy,col="red")

y<-c(0,1,2,2.1,2.2)
x<-c(2,-2,4,-10,4.1)
plot(x,y,pch=20,main="sort by y")
for (i in 1:4) {
  vx<-c(x[i],x[i+1])
  vy<-c(y[i],y[i+1])
  lines(vx,vy)
}
vx<-c(x[3],x[5])
vy<-c(y[3],y[5])
lines(vx,vy,col="red")