<template>
  <div>
    <Card :class="cardClass">
      <span slot="card-header" />
      <div class="bs-stepper">
        <div class="bs-stepper-header" role="tablist">
          <template v-for="(step, index) in steps">
            <div
              class="step"
              :key="`header-${index}`"
              :data-target="`stepper-content-${index}`"
              :class="index === activeStepIndex ? 'active' : null"
            >
              <button
                type="button"
                class="step-trigger d-flex flex-column justify-content-center align-items-center"
                role="tab"
                :id="`stepper-trigger-${index}`"
                :aria-controls="`stepper-content-${index}`"
                :disabled="index !== activeStepIndex"
                :class="index < activeStepIndex ? 'completed' : null"
              >
                <span class="stepper-circle">
                  <slot :name="'icon-' + index"/>
                </span>
                <span class="stepper-label" v-if="step.title">{{ step.title }}</span>
              </button>
            </div>
            <div
              class="bs-stepper-line"
              v-if="index + 1 !== steps.length"
              :key="`line-${index}`"
              :class="index < activeStepIndex ? 'completed' : null"
            />
          </template>
        </div>
        <div class="bs-stepper-content">
          <div
            :id="`stepper-content-${activeStepIndex}`"
            role="tabpanel"
            :aria-labelledby="`stepper-trigger-${activeStepIndex}`"
          >
            <transition-group name="fade">
              <div
                v-for="(step, index) in steps"
                v-show="index === activeStepIndex"
                :key="step.slotName"
              >
                <slot :name="step.slotName" />
              </div>
            </transition-group>
          </div>
        </div>
      </div>
    </Card>
    <div class="mt-4">
      <slot
        name="action-buttons"
        v-bind="stepperActionProps"
      >
        <button
          class="button alternative-button"
          @click.prevent="returnToPreviousStep"
          v-show="showReturnButton"
        >
          Voltar
        </button>
        <button
          class="button primary-button float-right"
          @click.prevent="tryProceedToNextStep"
          v-show="showProceedButton"
        >
          {{ proceedButtonText }}
        </button>
      </slot>
    </div>
  </div>
</template>

<script>
import { Card } from '@eniato-ui'

export default {
  components: { Card },
  props: {
    steps: {
      type: Array,
      default: () => []
    },
    onComplete: Function,
    cardClass: {
      type: String,
      default: ''
    },
    readOnly: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      activeStepIndex: 0
    }
  },
  computed: {
    isLastStep () {
      return this.activeStepIndex === this.lastStepIndex
    },
    lastStepIndex () {
      return this.steps.length - 1
    },
    currentStep () {
      return this.steps[this.activeStepIndex]
    },
    showReturnButton () {
      return this.activeStepIndex !== 0
    },
    showProceedButton () {
      return !this.readOnly || !this.isLastStep
    },
    proceedButtonText () {
      return !this.isLastStep ? 'Próximo' : 'Confirmar'
    },
    stepperActionProps () {
      return {
        clickReturn: this.returnToPreviousStep,
        showReturn: this.showReturnButton,
        clickNext: this.tryProceedToNextStep,
        showNext: this.showProceedButton,
        nextButtonText: this.proceedButtonText
      }
    }
  },
  methods: {
    returnToPreviousStep () {
      if (this.activeStepIndex > 0) {
        this.activeStepIndex -= 1
      } else {
        this.$emit('initial-step-return')
      }
    },
    tryProceedToNextStep () {
      if (this.readOnly) {
        this.proceedToNextStep()
      } else {
        this.currentStep.validate().then(valid => {
          if (valid) {
            this.proceedToNextStep()
          }
        })
      }
    },
    proceedToNextStep () {
      if (this.activeStepIndex < this.lastStepIndex) {
        this.activeStepIndex += 1
      } else if (this.activeStepIndex === this.lastStepIndex) {
        this.onComplete()
      }
    },
    setActiveStep (activeStepIndex) {
      if (activeStepIndex >= 0 && activeStepIndex < this.steps.length) {
        this.activeStepIndex = activeStepIndex
      }
    },
    async changeActiveStep (stepIndex) {
      if (stepIndex < 0 || stepIndex > this.steps.length - 1) {
        console.error(`Stepper.vue: Change Active Step Failed! Invalid step index "${stepIndex}".`)
      } else if (stepIndex > 0) {
        let count = 0
        while (count < stepIndex) {
          const valid = await this.steps[count].validate()
          if (!valid) {
            if (count !== stepIndex) {
              console.error(`Stepper.vue: Change Active Step Failed! Step index "${stepIndex}" does not have valid previous steps.`)
            }
            break
          }
          count += 1
        }
        this.setActiveStep(count)
      }
    }
  }
}
</script>

<style scoped>
.bs-stepper-header {
  padding-bottom: 1.25rem;
}

.stepper-label {
  color: var(--dark-color);
  margin-top: 4px;
}

.stepper-circle {
  width: 48px;
  height: 48px;
  border-radius: 100%;
  background-color: var(--elemental-color-2);
  display: flex;
  justify-content: center;
  align-items: center;
}

.completed .stepper-circle {
  background-color: var(--secondary-color);
}

.active .stepper-circle {
  background-color: var(--primary-color);
}

.fade-enter-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
