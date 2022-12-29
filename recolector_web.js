//Al buscar en página léxica.art

img = document.querySelector("body > div > div.mb-16.sm\\:mb-0.sm\\:mt-16 > div > div > div.w-full.mt-4.px-1.relative > div")

let images = []

//evento cuando cambie un elemto html desde js
img.addEventListener("DOMSubtreeModified", function() {
        //every children of img is div > a > div div img
        //print img.src
        for (let i = 0; i < img.children.length; i++) {
            let a = img.children[i].children[0].children[2].src
            if(images.indexOf(a) == -1){
                images.push(a)
                console.log(a)
                console.log(images.length)
            }
        }
    }
);


//código para copiar imagenes al final de la busqueda al portapapeles

/*
    let unique = [...new Set(images)]
    let data = {data: unique}
    copy(data)
*/