
var VIEW_HEIGHT, VIEW_WIDTH, REALM_HEIGHT, REALM_WIDTH;
var rowOffset, colOffset;
var myPanel, hoverBox, selectBox;
var zoneTypes = [], tileSize;
var tiles = [];


function load_context_data(_zoneTypes, _tileSize, _viewHeight, _viewWidth) {
    zoneTypes = _zoneTypes;
    tileSize = _tileSize;
    VIEW_HEIGHT = _viewHeight;
    VIEW_WIDTH = _viewWidth;
    REALM_HEIGHT = zoneTypes.length;
    REALM_WIDTH = zoneTypes[0].length;
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
        $('#zone-info').text('Selected: zone@r'+(row+rowOffset)+',c'+(column+colOffset))
    }
    return callback;
}

function initialize_panel() {
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
        for(var r = 0; r < VIEW_HEIGHT; r++) {
            var temp_row = [];
            for (var c = 0; c < VIEW_WIDTH; c++) {
                var tile = myPanel.createImage();
                tile.setLocationXY(tileSize * c, tileSize * r);
                tile.setHeight(tileSize);
                tile.setWidth(tileSize);
                tile.setUrl('/static/game/zones/0.png');
                tile.addMouseOverListener(make_hoverBox_callback(r, c));
                tile.addClickListener(make_selectBox_callback(r, c));
                myPanel.addElement(tile);
                temp_row.push(tile);
            }
            tiles.push(temp_row);
        }
        myPanel.addElement(hoverBox);
        myPanel.addElement(selectBox);
    }catch(err){
        console.log(err);
    }
}

function set_view(r_offset, c_offset, resetBoxes) {
    rowOffset = r_offset;
    colOffset = c_offset;
    for(var r = r_offset; r < r_offset+VIEW_HEIGHT; r++)
        for(var c = c_offset; c < c_offset+VIEW_WIDTH; c++){
            var tile = tiles[r-r_offset][c-c_offset];
            if (zoneTypes[r][c] == 0) {
                var meshing = (r == 0 || zoneTypes[r - 1][c] == 0 ? '' : 'N') +
                    (c == REALM_WIDTH - 1 || zoneTypes[r][c + 1] == 0 ? '' : 'E') +
                    (r == REALM_HEIGHT - 1 || zoneTypes[r + 1][c] == 0 ? '' : 'S') +
                    (c == 0 || zoneTypes[r][c - 1] == 0 ? '' : 'W');
                tile.setUrl('/static/game/zones/0_' + meshing + '.png');
            } else
                tile.setUrl('/static/game/zones/' + zoneTypes[r][c] + '.png');
        }
}

function move_view(dr, dc) {
    // hide the hover and selection boxes and clear the info box
    hoverBox.setLocationXY(-2*tileSize, -2*tileSize);
    selectBox.setLocationXY(-2*tileSize, -2*tileSize);
    $('#zone-info').text('');
    // move the view window, if possible
    if(rowOffset+dr < 0 || rowOffset+dr >= REALM_HEIGHT-VIEW_HEIGHT ||
            colOffset+dc < 0 || colOffset+dc >= REALM_WIDTH-VIEW_WIDTH)
        console.log('move_view ERROR: out of bounds');
    else
        set_view(rowOffset+dr, colOffset+dc);
}

$(document).ready(function() {
    rowOffset = 0;
    colOffset = 0;

    initialize_panel();
    set_view(0, 0);
});
