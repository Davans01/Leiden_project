<template>
  <page-wrapper>
    <h1>Home</h1>
  </page-wrapper>
  <page-footer></page-footer>
</template>



<script>
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"

export default {
  name: "debug",
  components: {
    PageWrapper,
    PageFooter,
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
}

.row.home-charts
  .full-row
  .blocks-container
  .block-group.content
  > .graphs-home {
  width: calc(50% - 15px);
}
</style>
