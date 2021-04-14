<template>
    <modal-base2>

    <div class="row chart-modal-2">

    <div class="full-row">

      <div class="blocks-container">
              <primary-button @click="close">close</primary-button>

        <div class="block title">
          <h1>Grafiek 2</h1>
        </div>
        
        <div class="block-group content">

          <div class="block content-chart">

            <div class="inner-block chart">
                  <chart2></chart2>

            </div>

          </div>

          <div class="block content-text">

            <div class="inner-block text">

              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
    </modal-base2>

</template>

<script>
import { modalBus } from "../bus"
import ModalBase2 from "../components/modal-base2"
import PrimaryButton from "../components/primary-button.vue"
import Chart2 from "../components/chart2.vue"

export default {
  name: "test-modal2",
  components: {
    ModalBase2,
    PrimaryButton,
    Chart2,
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
  &.chart-modal-2{

    .full-row{
      padding: 0 35px;
      width: 100%;
      float: left;
      margin: 0 auto;
    max-width: 1320px;

      .blocks-container{
        
        .primary-button{
          float: right;
        }
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
                    width: 50%;
                    float: left;
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