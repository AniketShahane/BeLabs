//ToolTips
const tooltips_elements = document.querySelectorAll('.tooltipped');
M.Tooltip.init(tooltips_elements, {});

//Collapsible Section
const collapses = document.querySelectorAll('.collapsible');
M.Collapsible.init(collapses, {});

//sideNav
const sidenavigation = document.querySelector('.sidenav');
M.Sidenav.init(sidenavigation, {});

//clickable images -- Single Blog Section
const imageboxed = document.querySelectorAll('.materialboxed');
M.Materialbox.init(imageboxed, {
  inDuration: 300,
  outDuration: 300
});

//Modal for creating new messages
const modal_elements = document.querySelectorAll('.modal');
M.Modal.init(modal_elements, {});


try {
  $('.count').each(function () {
    $(this).prop('Counter', 0).animate({
      Counter: $(this).text()
    }, {
        duration: 2000,
        easing: 'swing',
        step: function (now) {
          $(this).text(Math.ceil(now));
        }
      });
  });
}
catch (err) {
  console.log(err);
}
try {
  $('.alert_messages').fadeOut(5000, () => {
    //Animation chala bhai 
  });
}
catch (err) {
  console.log(err);
}

try {
  var objDiv = document.querySelector(".person_comments");
  objDiv.scrollTop = objDiv.scrollHeight;
}
catch (err) {
  console.log(err);
}
