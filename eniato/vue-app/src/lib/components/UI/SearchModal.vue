<template>
  <div ref="search-modal" class="search-modal" @keydown.enter="hide" @keydown.esc="hide" tabindex="0">
    <div class="blur"></div>
    <div class="search-wrapper" @click.stop>
      <button class="search-button">
        <SearchIcon class="search-icon" :height="20" :width="20" color="rgba(0, 0, 0, 0.7)" />
      </button>
      <input
        ref="search-input"
        v-model="filterQuery"
        placeholder="Busque pelo nome, CPF ou empresa"
        v-debounce:500ms="filterMethod" :debounce-events="['input', 'search']"
        class="search-input"
        @focusout="hide"
        type="search"
      />
      <button type="button" @mousedown.stop="clear" class="search-button clear-search-button">
        Limpar
      </button>
    </div>
  </div>
</template>
<script>
import { SearchIcon } from '@eniato-icons'

export default {
  name: 'SearchModal',
  components: {
    SearchIcon
  },
  data () {
    return {
      filterQuery: ''
    }
  },
  props: {
    filterMethod: {
      type: Function,
      default: () => {}
    }
  },
  methods: {
    open () {
      window.scrollTo({ top: 0 })
      this.$refs['search-modal'].classList.add('active')
      this.$nextTick(() => {
        this.$refs['search-input'].focus()
      })
    },
    hide (event) {
      event.preventDefault()
      this.$refs['search-modal'].classList.remove('active')
    },
    clear () {
      this.filterQuery = ''
    },
    getFilterQuery () {
      return this.filterQuery
    }
  }
}
</script>
<style scoped>
  .search-modal {
    opacity: 0;
    transition: opacity 0.3s;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 9999;
    overflow: hidden;
  }

  .search-modal.active {
    opacity: 1;
    height: 100%;
  }

  .search-modal.active .search-wrapper {
    margin-top: 70px;
    transition: margin 0.7s 0.3s;
  }

  .search-wrapper {
    border-radius:10px;
    position: relative;
    width: 50%;
    min-width: 260px;
    margin: 0 auto;
    padding: 2px 6px;
    margin-top: -50px;
    overflow: hidden;
    box-shadow: 0px 3px 7px rgba(0, 0, 0, 0.3);
    display: flex;
    align-items: center;
    background-color: rgb(255 255 255 / 40%);
    -webkit-backdrop-filter: blur(6px);
    backdrop-filter: blur(6px);
  }

  .search-input {
    background-color: transparent;
    color: rgba(0, 0, 0, 0.7);
    font-size: 22px;
    padding: 6px 12px 6px 0px;
    width: 100%;
    border: none;
  }

  .search-input::placeholder {
    opacity: 1;
    color: rgba(0, 0, 0, 0.3) !important;
  }

  .search-input:focus {
    outline: none;
  }

  .search-button, .search-button:focus, .search-button:active {
    outline:none;
    border: none;
    padding: 6px 12px;
    border: none;
    background-color: transparent;
  }

  .clear-search-button {
    position: absolute;
    right: 0;
    color: rgba(0, 0, 0, 0.4);
    transition: 0.2s;
  }

  .clear-search-button:hover {
    color: rgba(0, 0, 0, 0.6);
  }
</style>
