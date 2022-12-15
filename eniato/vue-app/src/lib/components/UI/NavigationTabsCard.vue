<template>
  <b-card no-body class="navigation-tabs-card" v-bind="$attrs">
    <b-tabs card fill>
      <b-tab v-for="tab in tabs" :key="tab.id" :title="tab.name" :active="tab.active">
        <b-card-text>
          <slot :name="tab.name">
            <div class="text-center mt-4 mb-4">
              <b-spinner variant="text-brmed-color" label="Text Centered"></b-spinner>
            </div>
          </slot>
        </b-card-text>
      </b-tab>
    </b-tabs>
  </b-card>
</template>

<script>
export default {
  inheritAttrs: true,
  props: {
    tabs: {
      name: String,
      active: {
        default: false,
        type: Boolean
      }
    }
  }
}
</script>

<style>
  .navigation-tabs-card .text-brmed-color,
  .navigation-tabs-card li.nav-item a.nav-link {
    color: #212529;
  }

  .navigation-tabs-card li.nav-item a.nav-link.active {
    font-weight: 500;
  }

  .navigation-tabs-card .card-header {
    color: #212529;
    margin: -26px -26px 0 -26px;
  }
</style>
