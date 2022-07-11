var origin_node         = undefined;
const global_limit      = 3;
const max_no_child      = 3;
const max_node_distance = 20;
const max_node_angle    = 360;

class Node{
    constructor(level, coordenates){
        this.x = coordenates[0];
        this.y = coordenates[1];
        console.log(`Coordenates: [ ${this.x}, ${this.y} ]`);

        this.child_nodes = [];
        if (level < global_limit){
            let no_child_nodes = Math.floor(Math.random() * max_no_child) + 1;
            console.log(`no_child_nodes: ${no_child_nodes}`);

            
            for (let i=1; i<= no_child_nodes; i++){
                console.group(`Children no ${i}`)
                let distance    = Math.floor( Math.random() * max_node_distance ) + 1;
                let angle       = Math.floor( Math.random() * max_node_angle ) + 1;
                let coordenates = this.coordenates([this.x, this.y], distance, angle);
                this.child_nodes.push( new Node(level + 1, coordenates) )
                console.groupEnd();
            }
        }

        // paintDot();
    }

    coordenates(origin, distance, angle){
        let origin_x = origin[0];
        let origin_y = origin[1];

        let x_distance = distance * Math.cos(angle);
        let y_distance = distance * Math.sin(angle);

        let x = Math.ceil(origin_x + x_distance);
        let y = Math.ceil(origin_y + y_distance);

        let coordenates = [x,y];
        return coordenates
    }
}



document.onmousedown = (e) => {
    const element = document.getElementById("test");
    const x = e.pageX;
    const y = e.pageY;
    element.innerHTML = `x: ${x} \t y: ${y}`;
    origin_node = new Node(1, [x,y]);
}
