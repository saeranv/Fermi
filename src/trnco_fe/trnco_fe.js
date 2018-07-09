//var myHeading = document.querySelector('h1');
//myHeading.textContent = 'Hi from JS world!';
/***
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
***/

var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'hello hyperspace!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
