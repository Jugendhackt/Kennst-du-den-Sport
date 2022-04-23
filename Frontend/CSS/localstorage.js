


        for (let i=0, iC=localStorage.length; i<iC; ++i) { 
            let storageKey = localStorage.key(i);
            console.log(storageKey + ' : ' + localStorage.getItem(storageKey) );
        }