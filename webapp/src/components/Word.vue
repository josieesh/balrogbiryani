<template>
  <div class="word">
    <label for="name">{{ numLetters }} letters</label>
    <br>
    <input type="text" id="guess" name="guess" required
       v-bind:minlength="numLetters" v-bind:maxlength="numLetters" size="14">
  </div>
</template>

<script>
const Http = new XMLHttpRequest();
const url='http://localhost:5000/randomword';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = function() {
    if(this.readyState==4 && this.status==200){
        console.log(Http.responseText)
    }
}

export default {
  name: 'Word',
  props: {
    numLetters: Number
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input {
text-align: center;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
