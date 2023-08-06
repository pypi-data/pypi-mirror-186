var scripts = [
"/page/js/jquery/1.10.2/jquery.min.js",
"/page/js/vue/vue.js",
//"/page/js/clipboard/clipboard.min.js"
]
var styles=[]

addStyle=(url)=>{
    var s = "<link href='"+url+"' type='text/css' rel='stylesheet'/>";
    document.write(s);
}
addScript=(url)=>{
    var s = "<script src='"+url+"'></script>";
    document.write(s);
}

addSrcs=(urls, addFc)=>{
    for(var index in urls){
        var script = urls[index]
        console.log("file to add: "+script)
        addFc(script)
    }
}
addScripts = (urls)=>{
    addSrcs(urls, addScript)
}

addStyles = (urls)=>{
    addSrcs(urls, addStyle)
}
addScripts(scripts)
addScript("/page/js/utils.js")

addStyles(styles)