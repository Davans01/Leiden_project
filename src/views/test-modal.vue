<template>
  <modal-base>
  <!-- <p>{{ testProp }}</p> -->
  <div class="row chart-modal">

    <div class="full-row">

      <div class="blocks-container">
              <primary-button @click="close">close</primary-button>

        <div class="block title">
          <h1>Grafiek 1</h1>
        </div>
        
        <div class="block-group content">

          <div class="block content-chart">

            <div class="inner-block chart">
              <chart :options="options"></chart>
              
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
  state() {
    return {
      options: {
        type: "doughnut",
        data: {
          labels: ["12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
          datasets: [
            {
              label: "# of Votes",
              data: [53, 3, 40, 3, 1, 24],
              backgroundColor: [
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
                "rgba(255, 159, 64, 0.2)",
              ],
              borderColor: [
                "rgba(255, 99, 132, 1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
                "rgba(255, 159, 64, 1)",
              ],
              borderWidth: 2,
            },
          ],
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
              },
            ],
          },
        },
      },
    }
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