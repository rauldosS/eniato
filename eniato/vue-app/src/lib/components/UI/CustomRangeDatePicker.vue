<template>
  <b-form-group v-bind="$attrs" :state="rangeState" :invalid-feedback="errors">
    <div class="row">
      <div class="col-sm-6">
        <b-form-group label="Início">
          <b-form-datepicker
            locale="pt-br"
            :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
            placeholder="Selecione..."
            :value="startDate"
            @input="date => $emit('update:start-date', date)"
            :disabled="disabled"
            :state="state"
            :required="required"
          />
        </b-form-group>
      </div>
      <div class="col-sm-6">
          <b-form-group label="Fim">
            <b-form-datepicker
              locale="pt-br"
              :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
              placeholder="Selecione..."
              :value="endDate"
              @input="date => $emit('update:end-date', date)"
              :disabled="disabled"
              :state="state"
              :required="required"
            />
          </b-form-group>
      </div>
    </div>
  </b-form-group>
</template>

<script>
import Moment from 'moment'

export default {
  props: {
    disabled: {
      type: Boolean,
      default: false
    },
    required: {
      type: Boolean,
      default: false
    },
    startDate: String,
    endDate: String,
    state: {
      type: Boolean,
      default: null
    }
  },
  data () {
    return {
      errors: null,
      rangeState: this.state
    }
  },
  methods: {
    validate () {
      this.rangeState = Moment(this.endDate, 'YYYY-MM-DD').isSameOrAfter(Moment(this.startDate, 'YYYY-MM-DD'))
      if (!this.rangeState) this.errors = 'Data de fim deve ser maior que a data de início'
      return this.rangeState
    }
  }
}
</script>
