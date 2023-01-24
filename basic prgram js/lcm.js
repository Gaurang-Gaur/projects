function lcm(a,b)
    {
        
        max=(a>b)?a:b;
        while(true){
        
            if((max%a==0)&&(max%b==0)){
                
                console.log(`lcm of ${a} and ${b} is:${max}`);
                break;
            }
            ++max;
        }
        
    }
lcm(34,23);