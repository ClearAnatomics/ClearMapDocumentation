/*
 * sidebar.js
 * ~~~~~~~~~~
 *
 */

$(function() {
  // global elements used by the functions.
  // the 'sidebarbutton' element is defined as global after its
  // creation, in the add_sidebar_button function
  var bodywrapper = $('.bodywrapper');
  var sidebar = $('.sphinxsidebar_right');
  var sidebarwrapper = $('.sphinxsidebarwrapper_right');

  // for some reason, the document has no sidebar; do not run into errors
  if (!sidebar.length) return;

  // original margin-left of the bodywrapper and width of the sidebar
  // with the sidebar expanded
  var bw_margin_expanded = bodywrapper.css('margin-right');
  var sb_width_expanded = sidebar.width();
  
  // margin-left of the bodywrapper and width of the sidebar
  // with the sidebar collapsed  
  var sidebar_outer_margin = 10;
  var sidebarbutton_width = 10;
  var sidebarbutton_separation = 5;

  var bw_margin_collapsed = sidebar_outer_margin + sidebarbutton_width + sidebar_outer_margin;
  var sb_width_collapsed = sidebarbutton_width + sidebar_outer_margin;


  // colors used by the current theme
  var dark_color = $('.related').css('background-color');
  var light_color = $('.document').css('background-color');

  function sidebar_is_collapsed() {
    return sidebarwrapper.is(':not(:visible)');
  }

  function toggle_sidebar() {
    if (sidebar_is_collapsed())
      expand_sidebar();
    else
      collapse_sidebar();
  }

  function collapse_sidebar() {
    sidebarwrapper.hide();
    sidebar.css('width', sb_width_collapsed);
    bodywrapper.css('margin-right', bw_margin_collapsed);
    sidebarbutton.css({
        'height': bodywrapper.height()
    });
    sidebarbutton.find('span').text('«');
    sidebarbutton.attr('title', _('Expand sidebar'));
    // document.cookie = 'sidebar_right=collapsed';
    localStorage.setItem("sidebar", "collapsed");
  }

  function expand_sidebar() {
    bodywrapper.css('margin-right', bw_margin_expanded);
    sidebar.css('width', sb_width_expanded);
    sidebarwrapper.show();
    sidebarbutton.css({
        'height': sidebar.height()
    });
    sidebarbutton.find('span').text('»');
    sidebarbutton.attr('title', _('Collapse sidebar'));
    //document.cookie = 'sidebar_right=expanded';
    localStorage.setItem("sidebar", "expanded");
  }

  function add_sidebar_button() {
    sidebarwrapper.css({
        'float': 'right',
        'margin-right' : sidebar_outer_margin
    });
    // create the button
    sidebar.append(
        '<div id="sidebarbutton"><span>&raquo;</span></div>'
    );
    var sidebarbutton = $('#sidebarbutton');
    light_color = sidebarbutton.css('background-color');
    sidebarbutton.find('span').css({
        'display': 'block',
        'margin' : '0px'
    });

    sidebarbutton.click(toggle_sidebar);
    sidebarbutton.attr('title', _('Collapse sidebar'));
    sidebarbutton.css({
        'color': '#000000',
        'background-color' : '#ccc',
        'font-size': '1.2em',
        'cursor': 'pointer',
        'float' : 'left',
        'height': sidebar.height(),
        'padding': '0px',
        'margin' : '14px 0px 14px 0px'
    });

    sidebarbutton.hover(
      function () {
          $(this).css('background-color', '#336699');
      },
      function () {
          $(this).css('background-color', '#ccc');
      }
    );
  }

  function set_position_from_cookie() {
    if (typeof(Storage) !== "undefined") {
        // Save the state of the sidebar as "open"
        var value = localStorage.getItem("sidebar");
        if ((value == 'collapsed') && (!sidebar_is_collapsed()))
          collapse_sidebar();
        else if ((value == 'expanded') && (sidebar_is_collapsed()))
          expand_sidebar();
      }

     /*    if (!document.cookie)
      return;
    var items = document.cookie.split(';');
    for(var k=0; k<items.length; k++) {
      var key_val = items[k].split('=');
      var key = key_val[0].replace(/ /, "");  // strip leading spaces
      if (key == 'sidebar') {
        var value = key_val[1];
        if ((value == 'collapsed') && (!sidebar_is_collapsed()))
          collapse_sidebar();
        else if ((value == 'expanded') && (sidebar_is_collapsed()))
          expand_sidebar();
      }
    }*/
  }

  add_sidebar_button();
  var sidebarbutton = $('#sidebarbutton');
  set_position_from_cookie();
});



// intelligent scrolling of the sidebar content
$(window).scroll(function() {
  var sb = $('.sphinxsidebarwrapper');
  var win = $(window);
  var sbh = sb.height();
  var offset = $('.sphinxsidebar').position()['top'];
  var wintop = win.scrollTop();
  var winbot = wintop + win.innerHeight();
  var curtop = sb.position()['top'];
  var curbot = curtop + sbh;
  // does sidebar fit in window?
  if (sbh < win.innerHeight()) {
    // yes: easy case -- always keep at the top
    sb.css('top', $u.min([$u.max([0, wintop - offset - 10]),
                          $(document).height() - sbh - 200]));
  } else {
    // no: only scroll if top/bottom edge of sidebar is at
    // top/bottom edge of window
    if (curtop > wintop && curbot > winbot) {
      sb.css('top', $u.max([wintop - offset - 10, 0]));
    } else if (curtop < wintop && curbot < winbot) {
      sb.css('top', $u.min([winbot - sbh - offset - 20,
                            $(document).height() - sbh - 200]));
    }
  }
});
