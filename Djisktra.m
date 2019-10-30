m=[-1 2 8 -1 -1 -1
   -1 -1 5 3 -1 -1
   -1 6 -1 -1 0 -1
   -1 -1 1 -1 7 6
   -1 -1 -1 4 -1 -1
   -1 -1 -1 -1 2 -1];

s=[1 2 3 4 6];
f=5;
act=5;
v=[100000 100000 100000 100000 0 100000];
route=[0 0 0 0 5 0];

while ~isempty(s)
    
    minval=100000;
    theMin=0;
    
    for i=1:length(s)
   
        if m(s(i),act)>-1
       
            if v(s(i))>v(act)+m(s(i),act)
                
                v(s(i))=v(act)+m(s(i),act);
                route(s(i))=act;
                
            end
        end
        
    end
    
    for i=1:length(s)
   
        if v(s(i))<=minval
           
            minval=v(s(i));
            theMin=i;
            
        end
        
    end
    
    act=s(theMin);
    f(length(f)+1)=act;
    s(theMin)=[];
    
end

route
v