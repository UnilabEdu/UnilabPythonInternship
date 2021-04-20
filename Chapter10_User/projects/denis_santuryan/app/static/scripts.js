function displayUploaded(input, format) {
    // show preview of uploaded pictures

    if (format === "profile_picture") {
        var w = 100
        var h = 100
        var preview_target = '#uploaded-profile-picture'
    } else if (format === "post_picture") {
        var w = 280
        var h = 210
        var preview_target = '#uploaded-post-picture'
    }
    
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $(preview_target)
                .attr('src', e.target.result)
                .width(w)
                .height(h);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

// dynamically increase height of post-input
var input = document.querySelector('.post-input');
input.addEventListener('input', resizeInput);
resizeInput.call(input);


function resizeInput() {
  var numberOfNL = (this.value.match(/\n/g)||[]).length
  this.style.height = 5 + this.value.length * 0.015 + numberOfNL*1.5 + "em" ;
}
// end //



// resize timeline images to acceptable dimensions
var pic = document.getElementById("posts").querySelectorAll(".timeline-picture");
pic.forEach(function(p) {
    var w = p.naturalWidth
    var h = p.naturalHeight
    if (w >= h) {
        var ratio = w / h
        if (w > 700) {
            w = 700
            h = 700 / ratio
        }
    }
    else if (h > w) {
        var ratio = h / w
        if (h > 600) {
            h = 600
            w = 600 / ratio
        }
    }
    var h = Math.round(h/16)
    var w = Math.round(w/16)
    p.style.height = h + 'rem'
    p.style.width = w + 'rem'
    p.style.marginRight = (48-w)/2 + 'rem'
    p.style.marginLeft = (48-w)/2 + 'rem'
});
