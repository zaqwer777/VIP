var annotations_map = new Object()

function generate_id(annotation) {
  var id = annotation.text.substring(0,1) + annotation.text.length;
  var randint = Math.floor(Math.random() * 10000);
  id += randint + annotation.text.substring(annotation.text.length - 1, annotation.text.length);
  return id;
}

function store_annotations() {
  for (var key in annotations_map) {
    var username = firebase.auth().currentUser.email.split('@')[0];
    firebase.database().ref('users/' + username + '/' + key).set(annotations_map[key]);
  }
}

function handle_data() {
  anno.addHandler('onAnnotationCreated', function(annotation) {
    var geometry = annotation.shapes[0].geometry;
    console.log(annotation);
    unique_id = generate_id(annotation);
    annotations_map[unique_id] = annotation;
    console.log(annotations_map);
  });
  anno.addHandler('onAnnotationRemoved', function(annotation) {
    var del_id = 0;
    var found = false;
    for (var key in annotations_map) {
      console.log(annotations_map);
      console.log(key);
      if (annotations_map[key].shapes[0].geometry == annotation.shapes[0].geometry) {
        found = true;
        del_id = i;
      }
    }
    if (del_id > -1 && found) {
      delete annotations_map[del_id];
    }
  });
  anno.addHandler('onAnnotationUpdated', function(annotation) {
    var update_id = 0;
    var found = false;
    for (var key in annotations_map) {
      if (annotations_map[key].shapes[0].geometry == annotation.shapes[0].geometry) {
        found = true;
        update_id = i;
      }
    }
    if (update_id > -1 && found) {
      annotations_map[update_id] = annotation;
    }
  });
}
