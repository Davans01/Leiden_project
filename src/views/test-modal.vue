<template>
  <modal-base>
  <!-- <p>{{ testProp }}</p> -->
  <div class="row chart-modal">

    <div class="full-row">

      <div class="blocks-container">

        <div class="block title">
          <h1>test modal</h1>
        </div>
        
        <div class="block-group content">

          <div class="block content-chart">

            <div class="inner-block chart">
              <chart></chart>
            </div>

          </div>

          <div class="block content-text">

            <div class="inner-block text">

              <p>test</p>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
     
      <primary-button @click="close">close</primary-button>
  </modal-base>
</template>

<script>
import { modalBus } from "../bus"
import ModalBase from "../components/modal-base"
import PrimaryButton from "../components/primary-button.vue"
import Chart from "../components/chart.vue"

export default {
  name: "test-modal",
  components: {
    ModalBase,
    PrimaryButton,
    Chart,
  },
  props: {
    testProp: Number,
  },
  methods: {
    close() {
      modalBus.emit("close")
    },
  },
}
</script>
<style lang="scss" scoped>

.backdrop{

  .modal{
    background-color: red;
    background: red!important;
    padding: 0px!important;
    border-radius: 4px;
    max-width: 100%!important;
    max-height: 100%!important;
    width: 100%!important;
    height: 100%!important;
  }
}

.modal[data-v-a8d280fe] {
    background: red!important;
    padding: 0px!important;
    border-radius: 4px;
    max-width: 100%!important;
    max-height: 100%!important;
    width: 100%!important;
    height: 100%!important;
}

.row{
  width: 100%;
  &.chart-modal{

    .full-row{
      margin: 0 auto;
      max-width: 1080px;
      padding: 0 35px;
      width: 100%;
      float: left;

      .blocks-container{
        
        .block{

          &.title{
            
            h1{
              color: red;
              text-transform: uppercase;
              font-weight: bold;
            }

          }
        }
        .block-group{

          &.content{

            .block{

              &.content-chart{

                .inner-block{

                  &.chart{

                  }
                }
              }
              
              &.content-text{
                
                .inner-block{

                  &.text{

                    p{

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
}
</style>