<template>
  <div id="balloon-container" ref="balloonContainer"></div>
</template>

<script>
export default {
  methods: {
    random (num) {
      return Math.floor(Math.random() * num)
    },
    getRandomStyles () {
      const r = this.random(255)
      const g = this.random(255)
      const b = this.random(255)
      const mt = this.random(200)
      const ml = this.random(50)
      const dur = this.random(5) + 5
      return `
        background-color: rgba(${r},${g},${b},0.7);
        color: rgba(${r},${g},${b},0.7); 
        box-shadow: inset -7px -3px 10px rgba(${r - 10}, ${g - 10}, ${b - 10}, 0.7);
        margin: ${mt}px 0 0 ${ml}px;
        animation: float ${dur}s ease-in infinite
      `
    },
    createBalloons (num) {
      for (let i = num; i > 0; i--) {
        const balloon = document.createElement('div')
        balloon.className = 'balloon'
        balloon.style.cssText = this.getRandomStyles()
        this.$refs.balloonContainer.append(balloon)
      }
    }
  },
  mounted () {
    this.createBalloons(100)
  }
}
</script>

<style>
  body {
    margin: 0;
  }

  #balloon-container {
    height: 100vh;
    padding: 1em;
    box-sizing: border-box;
    display: flex;
    flex-wrap: wrap;
    overflow: hidden;
    width: 100%;
    height: 100%;
    z-index: 10;
    top: 0;
    left: 0;
    position: fixed;
  }

  .balloon {
    height: 125px;
    width: 105px;
    border-radius: 75% 75% 70% 70%;
    position: relative;
  }

  .balloon:before {
    content: "";
    height: 75px;
    width: 1px;
    padding: 1px;
    background-color: #FDFD96;
    display: block;
    position: absolute;
    top: 125px;
    left: 0;
    right: 0;
    margin: auto;
  }

  .balloon:after {
      content: "▲";
      text-align: center;
      display: block;
      position: absolute;
      color: inherit;
      top: 120px;
      left: 0;
      right: 0;
      margin: auto;
  }

  @keyframes float {
    from {transform: translateY(100vh);
    opacity: 1;}
    to {transform: translateY(-300vh);
    opacity: 0;}
  }
</style>
