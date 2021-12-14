<template>
  <div id="app">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <Navbar/>
    <ListRegAns/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/Navbar.vue';
import ListRegAns from './components/ListRegAns.vue';

export default {
  name: 'App',
  components: {
    // HelloWorld,
    Navbar,
    ListRegAns,
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
