<template>
  <footer id="main-footer">
    <div class="row top footer">
      <div class="full-row">
        <div class="blocks-container">
          <div class="block-group content">
            <div class="block left">
              <h2>Universal Greenfields, meesters in groen.</h2>
            </div>

            <div class="block right">
              <div class="inner-block title">
                <h4>Universal Greenfields</h4>
                <p>&nbsp;</p>
              </div>

              <div class="inner-block text">
                <p>1e Mientlaan 11</p>
                <p>2223LG Katwijk</p>
                <p>&nbsp;</p>
                <p>Telefoon: 071-3646111</p>
                <p>Website: www.universalgreenfields.nl</p>
                <p>Email: info@universalgreenfields.nl</p>
                <p>KvK Leiden 281.05.541</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row bottom footer">
      <div class="full-row">
        <div class="blocks-container">
          <div class="block copyright">
            <p>&copy; Universal Greenfields 2021</p>
          </div>
          <div class="block developed">
            <p>Ontwikkeld door <span style="font-weight: 600">DIF</span></p>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "page-footer",
}
</script>

<style lang="scss" scoped>
.row {
  &.top {
    margin-top: 32px;

    &.footer {
      background-color: #6fcf97;
      width: 100%;
      float: left;

      .full-row {
        margin: 0 auto;
        max-width: 960px;
        .blocks-container {
          .block-group {
            &.content {
              width: 100%;

              .block {
                &.left {
                  float: left;
                  color: #fff;
                  margin-top: 90px;
                  max-width: 50%;

                  h2 {
                    margin: 0;
                    width: 50%;
                  }
                }

                &.right {
                  text-align: right;
                  float: right;
                  margin: 50px 0;
                  max-width: 50%;

                  h4 {
                    margin: 0;
                  }

                  p {
                    margin: 0;
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  &.bottom {
    &.footer {
      background-color: #57bc81;
      width: 100%;
      float: left;

      .full-row {
        margin: 0 auto;
        max-width: 960px;
        .blocks-container {
          .block {
            &.copyright {
              float: left;
              margin: 10px 0;
              color: #383737;
              max-width: 50%;

              p {
                margin: 0;
              }
            }
            &.developed {
              float: right;
              margin: 10px 0;
              color: #383737;
              max-width: 50%;

              p {
                margin: 0;
              }
            }
          }
        }
      }
    }
  }
}
</style>
