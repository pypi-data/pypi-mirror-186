$.count = 0;
function sleep(ms) {    
    return new Promise(resolve => setTimeout(resolve, ms));
}
repeat=(ms, fc)=>{
    setInterval(fc, ms);
}
async function test() {
    while($.count>0){
        await sleep(100);
    }
}

newVue=async (args)=>{
    await sleep(1);
    while($.count>0){
        await sleep(100);
    }
    args.el="#app"
    var vue=new Vue(args)
    _.vue = vue
    return vue;
}

$.jump=function(url){
    window.location.href=url;
}

function sleepx(ms){
    var t = Date.now();
    while(Date.now() - t <= ms);
}

$.component=(url, id=null)=>{
    $.count+=1;
    if(url.search(".html")<0){
        url = url+".html"
    }
    if(id == null){
        arr = url.split("/")
        id = arr[arr.length-1]
        id = id.split(".")[0]
    }
    var key = "#"+id;
    $.get(url,(rst)=>{
        var items = $(rst);
        items.appendTo(document.body);
        $.count-=1;
        return;
    })
    return this;
}
let component = $.component;
$.submit=function(url, maps){
    var body=$(document.body);
    var form = $("<form method='post'></form>");
    var input;
    form.attr({"action":url})
    $.each(maps, (key, value)=>{
        input = $("<input type='hodden'>");
        input.attr({"name":key});
        input.val(value)
        form.append(input)
    });
    form.appendTo(document.body);
    form.submit();
    document.body.removeChild(form[0]);
}

$.json=(url, data, success, error= (msg)=>{
    console.log("error in $.json");
    console.log(msg);
    console.log(msg.responseText)
    }
)=>{
    data= JSON.stringify(data);
    $.ajax({
        type:"POST",
        url:url,
        contentType:"application/json;charaset=utf-8",
        data:data,
        dataType:"json",
        success:success,
        error:error
    })
}
//document.addEventListener('readystatechange', () => console.log(document.readyState))

let _={
    sleep:(ms)=>{
        return new Promise(resolve => setTimeout(resolve, ms));
    },
    cache:{
        set(key,val){
            var s = _.jd(val)
            //console.log("[LOG] _.cache.set('"+key+"'):["+s+"]")
            window.localStorage[key]=s;
        },
        get(key){
            var val = window.localStorage[key];
            //console.log("[LOG] _.cache.get('"+key+"'):["+val+"]:"+typeof(val))
            if (val==null){
                return val;
            }
            var obj=null;
            try{
                obj = _.jl(val);
            }catch(err){
                console.log("[LOG] Error in _.jsonloads:")
                console.log(err)
            }
            //console.log("[LOG] _.jl:")
            //console.log(obj)
            return obj;
        }
    },
    key:{
        data:"_.data",
        stack:"_.stack",
        local:"_.local"
    },
    cleanCache(){
        for(var k in _.key){
            var key = _.key[k];
            _.cache.set(key, null)
        }
    },
    jsonloads(s){
        return $.parseJSON(s);
    },
    jsondumps(obj){
        return JSON.stringify(obj);
    },
    jl(s){
        return $.parseJSON(s);
    },
    jd(obj){
        return JSON.stringify(obj);
    },
    jump:(url, data=null)=>{
        console.log("jump:"+url)
        console.log("data:"+data)
        console.log(data)
        _.cache.set(_.key.data, data);
        if (_.cache.get(_.key.stack) == null){
            _.cache.set(_.key.stack, [])
        }
        var stack = _.cache.get(_.key.stack);
        stack = stack.concat(window.location.href);
        _.cache.set(_.key.stack, stack)
        window.location.href=url;
    },
    back:(data=null)=>{
        console.log("back:")
        console.log(data)
        var stack = _.cache.get(_.key.stack);
        if (stack.length==0){
            return;
        }
        var url = stack[stack.length-1]
        stack.pop();
        _.cache.set(_.key.stack, stack);
        _.cache.set(_.key.data, data);
        window.location.href=url;
    },
    onload:(fc)=>{
        _._onload = fc
    },
    _onload:()=>{

    },
    tryload:()=>{
        data = _.cache.get(_.key.data);
        if (data==null){
            return;
        }
        _.data = data;
        _._onload()
        return data;
    },
    load:()=>{
        data = _.cache.get(_.key.data)
        //_.cache.set(_.key.data, null)
        if (data==null){
            data={};
        }
        _.data = data;
        _._onload()
        return data;
    },
    local:{
        clean(){
            _.cache.set(_.key.local, {})
        },
        save:(key, val)=>{
            if( _.cache.get(_.key.local)==null){
                _.cache.set(_.key.local, {})
            }
            var dict = _.cache.get(_.key.local)
            dict[key] = val;
            _.cache.set(_.key.local, dict)
        },
        load:(key)=>{
            if( _.cache.get(_.key.local)==null){
                _.cache.set(_.key.local, {})
            }
            var dict = _.cache.get(_.key.local)
            return dict[key]
        }
    },
    submit:function(url, maps){
        var body=$(document.body);
        var form = $("<form method='post'></form>");
        var input;
        form.attr({"action":url})
        $.each(maps, (key, value)=>{
            input = $("<input type='hodden'>");
            input.attr({"name":key});
            input.val(value)
            form.append(input)
        });
        form.appendTo(document.body);
        form.submit();
        document.body.removeChild(form[0]);
    },
    copy(text){
        var input = document.createElement('input');
        input.value = text;
        document.body.appendChild(input);
        input.select();
        document.execCommand("Copy");
        document.body.removeChild(input);
    },
    $:(obj)=>{
        if (obj.name!=null){
            obj = $(obj)
        }
        return obj;
    }
}
window.onload=()=>{
    console.log("window.onload");
    _.load();
}
addScript("/page/js/utils_img.js")