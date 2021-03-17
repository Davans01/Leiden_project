<template>
    <page-footer id="main-footer">

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
                            </div>

                            <div class="inner-block text">
                                <p>1e Mientlaan 11</p>
                                <p>2223LG Katwijk</p>

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
    </page-footer>
</template>

<script>
export default {
  name: "page-footer",
}
</script>

<style lang="scss" scoped>
.row{

    &.top{

        &.footer{

            background-color: #6A8D00;
            position: relative;

            .full-row{
                margin: 0 auto;
                max-width: 1080px;
                padding: 0 35px;
                .blocks-container{

                    .block-group{

                        &.content{

                            .block{

                                &.left{

                                }

                                &.right{

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