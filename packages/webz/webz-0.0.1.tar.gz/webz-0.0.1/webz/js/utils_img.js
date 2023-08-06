
_.img={
    new:(path, id = null)=>{
        s = "<img"
        s += " src='"+path+"'"
        if (id != null){
            s += " id='"+id+"'"
        }
        s += ">"
        var img = $(s);
        img.appendTo(document.body);
        return _.img.build(img);
    },
    size:()=>{
        height = document.body.clientHeight;
        width = document.body.clientWidth;
        return [width, height];
    },
    rate:(pos)=>{
        size = _.img.size()
        return [pos[0]/size[0], pos[1]/size[1]]
    },
    s2v:(s)=>{
        var i = s.search("px");
        if(i>=0){
            s = s.substring(0, i) 
        }
        var v = Number(s);
        if(v!=v){
            return s;
        }
        return v;
    },
    $:(id, abs=true)=>{
        return _.img.build($(id), abs);
    },
    f2p:(v)=>{
        if(typeof(v)=='number'){
            if (v<=1){
                v *= 100;
            }
            v += "%";
        }
        return v;
    },
    p2f:(v)=>{
        if(typeof(v)=='string'){
            i = v.search("%")
            if(i>=0){
                v = v.substring(0, i);
            }
            v = Number(v)/100;
        }
        return v;
    },
    Image:function(img, abs=true){
        img = _.$(img)
        this.src = img;
        this.angle = 0;
        if (abs){
            img.css("position", "absolute");
        }
        function Angle(tmp){
            this._angle = 0;
            this._up = tmp;
            this._modify = ()=>{
                v = Math.trunc(this._angle/360)
                this._angle -= v*360;
                if(this._angle<0){
                    this._angle += 360;
                }
                img = this._up.src;
                s = "rotate("+this._angle+"deg)";
                styles = ["webkitTransform","MozTransform","msTransform","OTransform","transform"]
                for(var i in styles){
                    var key = styles[i];
                    img.css(key, s);
                }
            }
            this.set = (angle)=>{
                this._angle = angle;
                this._modify();
            }
            this.add=(angle)=>{
                this._angle += angle;
                this._modify();
            }
        }
        this.angle = new Angle(this);
        this.rotate = (angle)=>{
            this.angle.set(angle);
            return this
        }
        this.move = (pos)=>{
            img = this.src;
            img.css("left", ""+pos[0]);
            img.css("top", ""+pos[1]);
            return this
        }
        this.rmove=(pos)=>{
            pos = [_.img.f2p(pos[0]), _.img.f2p(pos[1])]
            return this.move(pos);
        }
        this.resize = (size)=>{
            img = this.src;
            img.css("width", ""+size[0]);
            img.css("height", ""+size[1]);
            this._rate = this.rate();
            //console.log("resize:"+this.rate()+":"+size[0]/(size[1]+0.001))
            return this
        }
        this.scale=(rate)=>{
            size = this.size();
            size = [size[1]*rate*this._rate, size[1]*rate]
            img = this.src;
            img.css("width", ""+size[0]);
            img.css("height", ""+size[1]);
        }
        this.pos=()=>{
            img = this.src;
            x = img.css("left");
            y = img.css("top");
            x = _.img.s2v(x)
            y = _.img.s2v(y)
            return [x, y];
        }
        this.size=()=>{
            img = this.src;
            width = img.css("width");
            height = img.css("height");
            width = _.img.s2v(width)
            height = _.img.s2v(height)
            return [width, height];
        }
        this.rate = ()=>{
            size = this.size();
            return size[0]/(size[1]+0.000001)
        }
        this._rate = this.rate();
    },
    build:(img, abs = true)=>{
        return new _.img.Image(img, abs);
        img = _.$(img)
        let tmp = {src:img};
        tmp.angle = 0;
        if (abs){
            img.css("position", "absolute");
        }
        function Angle(tmp){
            this._angle = 0;
            this._up = tmp;
            this._modify = ()=>{
                v = Math.trunc(this._angle/360)
                this._angle -= v*360;
                if(this._angle<0){
                    this._angle += 360;
                }
                img = this._up.src;
                s = "rotate("+this._angle+"deg)";
                styles = ["webkitTransform","MozTransform","msTransform","OTransform","transform"]
                for(var i in styles){
                    var key = styles[i];
                    img.css(key, s);
                }
            }
            this.set = (angle)=>{
                this._angle = angle;
                this._modify();
            }
            this.add=(angle)=>{
                this._angle += angle;
                this._modify();
            }
        }
        tmp.angle = new Angle(tmp);
        tmp.rotate = (angle)=>{
            tmp.angle.set(angle);
            return tmp
        }
        tmp.move = (pos)=>{
            img = tmp.src;
            img.css("left", ""+pos[0]);
            img.css("top", ""+pos[1]);
            return tmp
        }
        tmp.rmove=(pos)=>{
            pos = [_.img.f2p(pos[0]), _.img.f2p(pos[1])]
            return tmp.move(pos);
        }
        tmp.resize = (size)=>{
            img = tmp.src;
            img.css("width", ""+size[0]);
            img.css("height", ""+size[1]);
            return tmp
        }
        tmp.scale=(rate)=>{
            size = tmp.size();
            size = [size[0]*rate, size[1]*rate]
            tmp.resize(size);
        }
        tmp.pos=()=>{
            img = tmp.src;
            x = img.css("left");
            y = img.css("top");
            x = _.img.s2v(x)
            y = _.img.s2v(y)
            return [x, y];
        }
        tmp.size=()=>{
            img = tmp.src;
            width = img.css("width");
            height = img.css("height");
            width = _.img.s2v(width)
            height = _.img.s2v(height)
            return [width, height];
        }
        return tmp;
    }
}