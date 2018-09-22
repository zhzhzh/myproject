<template>
  <div id="app">
    <img src="./assets/logo.png">
    <VueAudio />
    <router-view/>
  </div>
</template>

<script>
import VueAudio from './components/VueAudio'
export default {
  name: 'App',
  components: {
    VueAudio
  },
  data () {
    return {}
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
