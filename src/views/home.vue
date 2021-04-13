<template>
  <page-wrapper>
    <h1>home</h1>
    <div class="row home-charts">
    
      <div class="full-row">

        <div class="blocks-container">

          <div class="block title">
            <h2>Grafieken</h2>
          </div>

          <div class="block-group content">
            <div class="block graphs-home">
              <primary-button @click="openTestModal">
                <a class="modal-test">
                <img src="../../src/assets/test.jpg" />
                  <p>Grafiek 1</p>
                </a>
              </primary-button>
            </div>
           
           <div class="block graphs-home">
              <primary-button @click="openTestModal">
                <a class="modal-test">
                <img src="../../src/assets/test.jpg" />
                  <p>Grafiek 2</p>
                </a>
              </primary-button>
            </div>

          </div>
        </div>
      </div>
    </div>
  
    <!-- <chart></chart> -->
  </page-wrapper>
  <page-footer></page-footer>
</template>



<script>
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"
// import Chart from "../components/chart.vue"
import TestModal from "./test-modal.vue"
import { modalBus } from "../bus"



export default {
  name: "debug",
  components: {
    PageWrapper,
    PageFooter,
    // Chart,
  },
  data() {
    return {
      status: "unknown",
    }
  },
  computed: {
    state() {
      return JSON.stringify(this.$store.state, undefined, 2)
    },
  },
  methods: {
    openTestModal() {
      modalBus.emit("open", {
        component: TestModal,
        props: {
          testProp: Math.random(),
        },
      })
    },
  },
}

</script>

<style lang="scss" scoped>
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

  &.home-charts{
    width: 100%;
    float: left;
    .full-row{
      margin: 0 auto;
      max-width: 1080px;
      padding: 0 35px;
      width: 100%;
      float: left;
      .blocks-container{
        display: block;
        .block{

          .title{

            h2{

            }
          }
        }
        .block-group{
          
          &.content{
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
            .block{

              &.graphs-home{
                background-color: #fff;
                text-align: center;
                float: left;
                box-sizing: border-box;
                box-shadow: 3px 3px 8px 3px rgb(0 0 0 / 16%);
                margin-bottom: 30px;
                position: relative;
                cursor: pointer;
                a{
                  display: block;
                  padding-top: 100px;
                  img{
                    
                  }
                  p{
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
.row.home-charts .full-row .blocks-container .block-group.content > .graphs-home:nth-of-type(6n+1) {
    margin-right: 15px;
    margin-left: 0;
}
.row.home-charts .full-row .blocks-container .block-group.content > .graphs-home:nth-of-type(6n+2) {
    // margin-right: 15px;
    margin-left: 15px;
}

.row.home-charts .full-row .blocks-container .block-group.content > .graphs-home {
    width: calc(50% - 15px);
}

</style>
