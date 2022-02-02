<template>
  <div class="word">
    <label for="name">{{ numLetters }} letters</label>
    <br>
    <input type="text" id="guess" name="guess" required
        v-bind:minlength="numLetters" v-bind:maxlength="numLetters" size="14">
  </div>
</template>

<script>
// var numLetters = this.word.length()
// document.getElementById("guess").innerHTML = "".concat(numLetters, " letters") 
// document.getElementById("guess").setAttribute("minLength", numLetters);
// document.getElementById("guess").setAttribute("maxLength", numLetters);
export default {
  name: 'Word',
  props: {
    word: String
  },
  data() {
      return {
        numLetters: 0
      }
  },
  created() {
           this.numLetters = this.word.length;
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
