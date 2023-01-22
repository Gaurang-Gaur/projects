

function fib(n){
    let a=[];
        if(n==1){
            a.push(0);
        }
        else if(n==2){
            a.push(0);
            a.push(1);
            
        }
        else{
    a.push(0);
            a.push(1);
            a.push(1);
            let i=0;
            let j=0;
            let k=0;
            i=a[0];
            j=a[1];
            k=i+j;
            let b=0;
            while(b!=n-3){
                    i=j;   
            j=k;
                k=i+j;
                a.push(k);
                b++;
            }
         
                
            
            
        
        }
        return a;
    }
    fib(7);