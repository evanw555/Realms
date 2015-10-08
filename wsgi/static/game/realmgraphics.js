
var myPanel, hoverBox, zoneTypes = [];


function load_context_data(_zoneTypes) {
    zoneTypes = _zoneTypes;
}

$(document).ready(function() {
    try{
        myPanel = new jsgl.Panel(document.getElementById("canvas"));
        hoverBox = myPanel.createRectangle();
        hoverBox.setHeight(32);
        hoverBox.setWidth(32);
        hoverBox.getFill().setOpacity(0.0);
        hoverBox.getStroke().setWeight(3);

          /* Create circle and modify it */
        for(var r = 0; r < zoneTypes.length; r++)
            for(var c = 0; c < zoneTypes[r].length; c++){
                var tile = myPanel.createRectangle();
                tile.setLocationXY(32*c, 32*r);
                tile.setHeight(32);
                tile.setWidth(32);
                tile.getStroke().setWeight(0);
                tile.getFill().setColor("rgb(16,"+(zoneTypes[r][c]==1?255:0)+
                                            ","+(zoneTypes[r][c]==0?255:0)+")");
                tile.addMouseOverListener(function(event) {
                    hoverBox.setLocationXY(event.getSourceElement().getX(), event.getSourceElement().getY());
                });
                myPanel.addElement(tile);
            }
        myPanel.addElement(hoverBox);
        var label = myPanel.createLabel();
        label.setText("Welcome to this Realm!");
        label.setLocationXY(Math.floor(Math.random() * 400), Math.floor(Math.random() * 400));
        label.setBold(true);
        label.setFontFamily("sans-serif");
        label.setFontSize(24);
        myPanel.addElement(label);
    }catch(err){
        console.log("JSGL error");
    }
});