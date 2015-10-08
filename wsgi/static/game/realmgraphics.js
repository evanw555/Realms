
var myPanel, hoverBox;
var zoneTypes = [], tileSize;


function load_context_data(_zoneTypes, _tileSize) {
    zoneTypes = _zoneTypes;
    tileSize = _tileSize;
}

$(document).ready(function() {
    try{
        myPanel = new jsgl.Panel(document.getElementById("canvas"));
        myPanel.addMouseOutListener(function() {
            hoverBox.getStroke().setOpacity(0);
        });
        myPanel.addMouseOverListener(function() {
            hoverBox.getStroke().setOpacity(1);
        });

        hoverBox = myPanel.createRectangle();
        hoverBox.setHeight(tileSize);
        hoverBox.setWidth(tileSize);
        hoverBox.getFill().setOpacity(0.0);
        hoverBox.getStroke().setWeight(3);

          /* Create circle and modify it */
        for(var r = 0; r < zoneTypes.length; r++)
            for(var c = 0; c < zoneTypes[r].length; c++){
                var tile = myPanel.createRectangle();
                tile.setLocationXY(tileSize*c, tileSize*r);
                tile.setHeight(tileSize);
                tile.setWidth(tileSize);
                tile.getStroke().setWeight(0);
                tile.getFill().setColor("rgb(16,"+(zoneTypes[r][c]==1?255:0)+
                                            ","+(zoneTypes[r][c]==0?255:0)+")");
                tile.addMouseOverListener(function(event) {
                    hoverBox.setLocationXY(event.getSourceElement().getX(), event.getSourceElement().getY());
                });
                myPanel.addElement(tile);
            }
        myPanel.addElement(hoverBox);
    }catch(err){
        console.log("JSGL error");
    }
});