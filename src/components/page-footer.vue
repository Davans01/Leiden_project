<template>
  <footer>
    <page-wrapper class="section">
      <div class="content">
        <h2>Universal Greenfields, meesters in groen.</h2>
        <div class="contact">
          <p>
            Universal Greenfields
            <br />
            1e Mientlaan 11
            <br />
            2223&nbsp;LG&nbsp;&nbsp;Katwijk
          </p>
          <p>
            Tel: <a href="tel:31713646111">+31 79 3646111</a>
            <br />
            Web:
            <a href="https://universalgreenfields.nl/" rel="noopener">
              universalgreenfields.nl
            </a>
            <br />
            Mail:
            <a href="mailto:info@universalgreenfields.nl">
              info@universalgreenfields.nl
            </a>
            <br />
            KvK: 28105541
            <br />
          </p>
        </div>
      </div>
    </page-wrapper>
    <page-wrapper class="section copyright">
      <div class="content">
        <span>&copy; Universal Greenfields 2021</span>
        <span>Developed by <strong>DIF</strong></span>
      </div>
    </page-wrapper>
  </footer>
</template>

<script>
import PageWrapper from "./page-wrapper.vue"

export default {
  name: "page-footer",
  components: {
    PageWrapper,
  },
}
</script>

<style lang="scss" scoped>
@import "../vars.scss";

footer {
  margin-top: 32px;
}

.section {
  background: $accent;
  padding: 32px 0;

  &.copyright {
    background: darken($accent, 10%);
    padding: 16px 0;
  }
}

.content {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 32px;
  align-items: center;

  @media (min-width: 960px) {
    grid-template-columns: repeat(2, 1fr);

    & > *:last-child {
      justify-self: end;
      text-align: end;
    }
  }
}

.contact {
  & a {
    color: inherit;
  }
}
</style>
