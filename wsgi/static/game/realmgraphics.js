
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
        var realmHeight = zoneTypes.length;
        var realmWidth = zoneTypes[0].length;
        for(var r = 0; r < realmHeight; r++)
            for(var c = 0; c < realmWidth; c++){
                var tile = myPanel.createImage();
                tile.setLocationXY(tileSize*c, tileSize*r);
                tile.setHeight(tileSize);
                tile.setWidth(tileSize);
                if(zoneTypes[r][c] == 0){
                    var meshing = (r > 0 || zoneTypes[r-1][c] != 0 ? 'N' : '') +
                                    (c < realmWidth-1 || zoneTypes[r][c+1] != 0 ? 'E' : '') +
                                    (r < realmHeight-1 || zoneTypes[r+1][c] != 0 ? 'S' : '') +
                                    (c > 0 || zoneTypes[r][c-1] != 0 ? 'W' : '');
                    tile.setUrl('/static/game/zones/0_'+meshing+'.png');
                }else
                    tile.setUrl('/static/game/zones/'+zoneTypes[r][c]+'.png');
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