N=100;
K=40;
c=0;
h=5;
b=10;

demand=randi([1,20],1,N);
d=zeros(N,(N+1));
cost=zeros(N,(N+1));
costK=zeros(N,(N+1));

V=zeros(1,N+1);
des=zeros(1,N+1);

%Demand estimation

for i=1:(N)
   
    for j=(i+1):(N+1)
        
        d(i,j)=sum(demand(1,i:(j-1)));
    end
    
end

%Cost estimation

for i=1:N
   
   for j=(i+1):(N+1)
   
       theMinC=10000000;
       theK=0;
       
       for l=i:(j-1)
          
           value=K+c*d(i,j)+b*sum(d(i,(i):l))+h*sum(d((l+1):(j-1),j));
           
           if value<theMinC
              
               theMinC=value;
               theK=l;
               
           end
                      
       end
       
       cost(i,j)=theMinC;
       costK(i,j)=theK;
       
   end
   
end

%Algorithm
for i=1:N
   
    pos=N+1-i;
    theMinV=1000000;
    theMin=0;
    
    for j=(pos+1):(N+1)
       
        value=cost(pos,j) + V(1,j);
        
        if value<theMinV
           
            theMinV=value;
            theMin=j;
            
        end
        
    end
    
    V(1,pos)=theMinV;
    des(1,pos)=theMin;
        
end

result=des(1,1);
resultK=costK(1,des(1,1));
posAct=des(1,1);
produce=d(1,des(1,1));
while posAct<(N+1)

result(length(result)+1)=des(1,posAct);
resultK(length(resultK)+1)=costK(posAct,des(1,posAct));
produce(length(produce)+1)=d(posAct,des(1,posAct));
posAct=des(1,posAct);

end

V(1,1)
result
resultK
produce
