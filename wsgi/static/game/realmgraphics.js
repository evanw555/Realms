
var myPanel, hoverBox, selectBox;
var zoneTypes = [], tileSize;


function load_context_data(_zoneTypes, _tileSize) {
    zoneTypes = _zoneTypes;
    tileSize = _tileSize;
}

function make_hoverBox_callback(row, column) {
    function callback() {
        hoverBox.setLocationXY(column*tileSize, row*tileSize);
    }
    return callback;
}

function make_selectBox_callback(row, column) {
    function callback() {
        selectBox.setLocationXY(column*tileSize, row*tileSize);
        $('#zone-info').text('Selected: zone@r'+row+',c'+column)
    }
    return callback;
}

$(document).ready(function() {
    try{
        myPanel = new jsgl.Panel(document.getElementById("canvas"));
        myPanel.addMouseOutListener(function() {
            hoverBox.getStroke().setOpacity(0);
        });
        myPanel.addMouseOverListener(function() {
            hoverBox.getStroke().setOpacity(.2);
        });

        hoverBox = myPanel.createRectangle();
        hoverBox.setHeight(tileSize);
        hoverBox.setWidth(tileSize);
        hoverBox.setFill(jsgl.fill.DISABLED);
        hoverBox.getStroke().setOpacity(.2);
        hoverBox.getStroke().setWeight(3);

        selectBox = myPanel.createRectangle();
        selectBox.setHeight(tileSize);
        selectBox.setWidth(tileSize);
        selectBox.setFill(jsgl.fill.DISABLED);
        selectBox.getStroke().setWeight(2);

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
                    var meshing = (r == 0 || zoneTypes[r-1][c] == 0 ? '' : 'N') +
                                    (c == realmWidth-1 || zoneTypes[r][c+1] == 0 ? '' : 'E') +
                                    (r == realmHeight-1 || zoneTypes[r+1][c] == 0 ? '' : 'S') +
                                    (c == 0 || zoneTypes[r][c-1] == 0 ? '' : 'W');
                    tile.setUrl('/static/game/zones/0_'+meshing+'.png');
                }else
                    tile.setUrl('/static/game/zones/'+zoneTypes[r][c]+'.png');
                tile.addMouseOverListener(make_hoverBox_callback(r, c));
                tile.addClickListener(make_selectBox_callback(r, c));
                myPanel.addElement(tile);
            }
        myPanel.addElement(hoverBox);
        myPanel.addElement(selectBox);
    }catch(err){
        console.log(err);
    }
});