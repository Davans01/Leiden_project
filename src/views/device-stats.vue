<template>
  <page-wrapper>
    <pre>{{ JSON.stringify(device, undefined, 2) }}</pre>
    <pre>{{ JSON.stringify(measurements, undefined, 2) }}</pre>
    <h1>home</h1>
    <div class="row home-charts">
      <div class="full-row">
        <div class="blocks-container">
          <div class="block title">
            <h2>Grafieken</h2>
          </div>
          <div class="block-group content">
            <div
              class="block graphs-home"
              v-for="type of measureTypes"
              :key="type.id"
            >
              <primary-button @click="openMeasurementsModal(type)">
                <a class="modal-test">
                  <img src="../../src/assets/test.jpg" />
                  <p>Grafiek 1</p>
                </a>
              </primary-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </page-wrapper>
  <page-footer></page-footer>
</template>

<script>
import { mapState } from "vuex"
import PageFooter from "../components/page-footer.vue"
import PageWrapper from "../components/page-wrapper.vue"
import MeasurementsModal from "./measurements-modal.vue"
import { modalBus } from "../bus"

export default {
  name: "device-stats",
  components: {
    PageFooter,
    PageWrapper,
  },
  computed: {
    ...mapState({
      measureTypes(state) {
        return state.meta.measureTypes
      },
      device(state) {
        return (state.devices.devices || []).find(
          (device) => device.serial === this.$route.params.deviceId,
        )
      },
      measurements(state) {
        return state.devices.measurements[this.$route.params.deviceId]
      },
    }),
  },
  mounted() {
    if (!this.device) {
      this.$store.dispatch("fetchDevices")
    }
    if (!this.measurements) {
      this.$store.dispatch("fetchMeasurements", this.$route.params.deviceId)
    }
  },
  methods: {
    openMeasurementsModal(type) {
      modalBus.emit("open", {
        component: MeasurementsModal,
        props: {
          device: this.device,
          type,
        },
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.modal[data-v-a8d280fe] {
  background: red !important;
  padding: 0px !important;
  border-radius: 4px;
  max-width: 100% !important;
  max-height: 100% !important;
  width: 100% !important;
  height: 100% !important;
}
.row {
  &.home-charts {
    width: 100%;
    float: left;
    .full-row {
      margin: 0 auto;
      max-width: 1080px;
      padding: 0 35px;
      width: 100%;
      float: left;
      .blocks-container {
        display: block;
        .block-group {
          &.content {
            margin-top: 30px;
            display: -webkit-box;
            display: -moz-box;
            display: -webkit-flex;
            display: -ms-flexbox;
            display: flex;
            -webkit-flex-wrap: wrap;
            -ms-flex-wrap: wrap;
            flex-wrap: wrap;
            float: left;
            width: 100%;
            .block {
              &.graphs-home {
                background-color: #fff;
                text-align: center;
                float: left;
                box-sizing: border-box;
                box-shadow: 3px 3px 8px 3px rgb(0 0 0 / 16%);
                margin-bottom: 30px;
                position: relative;
                cursor: pointer;
                a {
                  display: block;
                  padding-top: 100px;
                  p {
                    padding-bottom: 40px;
                    margin-top: 30px;
                    letter-spacing: 2px;
                    font-size: 20px;
                    color: #5a5a5a;
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
.row.home-charts
  .full-row
  .blocks-container
  .block-group.content
  > .graphs-home:nth-of-type(6n + 1) {
  margin-right: 15px;
  margin-left: 0;
}
.row.home-charts
  .full-row
  .blocks-container
  .block-group.content
  > .graphs-home:nth-of-type(6n + 2) {
  margin-left: 15px;
  margin-right: 15px;
}
.row.home-charts
  .full-row
  .blocks-container
  .block-group.content
  > .graphs-home:nth-of-type(6n + 3) {
  margin-left: 15px;
}
.row.home-charts
  .full-row
  .blocks-container
  .block-group.content
  > .graphs-home:nth-of-type(6n + 4) {
  margin-right: 15px;
}
.row.home-charts
  .full-row
  .blocks-container
  .block-group.content
  > .graphs-home:nth-of-type(6n + 5) {
  margin-left: 15px;
  margin-right: 15px;
}

.row.home-charts
  .full-row
  .blocks-container
  .block-group.content
  > .graphs-home:nth-of-type(6n + 6) {
  margin-left: 15px;
}
.row.home-charts
  .full-row
  .blocks-container
  .block-group.content
  > .graphs-home {
  width: calc(33.3333333333% - 20px);
}
</style>
