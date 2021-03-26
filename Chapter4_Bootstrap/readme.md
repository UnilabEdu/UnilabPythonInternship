# [Bootstrap4](https://getbootstrap.com/)

### [შესავალი](https://getbootstrap.com/docs/4.5/getting-started/introduction/) | [მაგალითები](https://getbootstrap.com/docs/4.5/examples/) | [დოკუმენტაცია](https://getbootstrap.com/docs/4.5/layout/overview/)

Boostrap არის მსოფლიოში ერთ-ერთი ყველაზე პოპულარული ფრონტ-ენდ დეველოპმენტ იარაღების ნაკრები. იგი შექმნეს twitter -ის დეველოპერებმა. მას აქვს html ელემენტების და css სტილის მზა შაბლონები.

## როგორ გამოვიყენოთ Bootstrap

არსებობს Bootstrap-ის პროექტში ჩაშენების რამოდენიმე გზა.

- თქვენ შეგიძლიათ ინდივიდუალურად [გადმოწეროთ Bootstrat](https://getbootstrap.com/docs/4.5/getting-started/download/)
  სორს კოდთან და კომპონენტებთან ერთად.
- დააყენოთ რომელიმე სასურველი Package Manager-ის მეშვეობით (npm, yarn, RubyGems, NuGet, Composer).
- შემოიტანოთ შესაბამისი ბმულები html ფაილში, [BootstrapCDN](https://www.bootstrapcdn.com/) ის მეშვეობით.

### cdn -ით დაყენება

```html
<!-- in head section -->
<!-- Chapter3_CSS only -->
<link
  rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
  integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
  crossorigin="anonymous"
/>

<!-- at the end of the body section -->
<!-- JS, Popper.js, and jQuery -->
<script
  src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
  integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
  crossorigin="anonymous"
></script>
<script
  src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
  integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
  crossorigin="anonymous"
></script>
<script
  src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
  integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV"
  crossorigin="anonymous"
></script>
```

## [კომპონენტები](https://getbootstrap.com/docs/4.5/components/)

**კომპონენტი** Bootstrap-ში წინასწარ გამზადებული ვებ-გვერდ ელემენტია. [კომპონენტების დოკუმენტაციაში](https://getbootstrap.com/docs/4.5/components/) ნათლად არის თითოეული კომპონენტის გამოყენების ინსტრუქცია, დემონსტრაცია და კოდი განთავსებული,
რომელიც პირდაპირ შეგიძლია გადაწერო პროექტში, გააკეთო მასში ცვლილებები და მოარგო ვებ გვერდს.

### კონტეინერი

კონტეინერში შეგვიძლია მოვათავსოთ ნებისმიერი სახის კონტენტი. Bootstrap-ი მას ავტომატურად აძლევს ჩარჩოს, გამოყოფს გვერდიდნ
და ხდის რესფონსივს ეკრანის გაფართოების მიმართ.

```html
<div class="container">
    content
</div>
```

### [ღილაკები](https://getbootstrap.com/docs/4.5/components/buttons/)
Bootstrap-ში უამრავი სხვადასხვა ტიპისა და ვიზუალის ღილაკია მოთავსებული. დოკუმენტაციაში ნაჩვენები მაგალითებიდან
შეგიძლია აირჩიო სასურველი ღილაკის სტილი და მიუთითო მისი კლასი შენს მიერ გამოყენებულ ღილაკს. მაგალითად:

```html
<button type="button" class="btn btn-success">Success</button>
```

### [Jumbotron](https://getbootstrap.com/docs/4.5/components/jumbotron/)
ჯამბოტრონი გამოიყენება როგორც "შოუქეის" შეტყობინება ვებ გვერდზე. ეს კომპონენტი წარმოადგენს ერთგვარ ჰაილაითერ ბარათს,
რომელიც მომხმარებელს აწვდის მოკლე შეტყობინებას რესურსზე. მაგალითად:

```html
<div class="jumbotron">
  <h1 class="display-4">Hello, world!</h1>
  <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
  <hr class="my-4">
  <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
  <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
</div>
```

### [ფორმები](https://getbootstrap.com/docs/4.5/components/forms/)

ფორმები მომხმარებელსა და საიტს შორის საურთიერთობო უმიშვნელოვანესი ელემენტია. Bootstrap მდიდარია სხვადასხვა
სტილისა და ტიპის ფორმებით, რომელიც მზადაა გვერდზე განსათავსებლად.

რეგისტრაციის ფორმის მაგალითი:
```html
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### [navbar](https://getbootstrap.com/docs/4.5/components/navbar/)
თანამედროვე ვებ გვერდის მნიშვნელოვან ატრიბუტს წარმოადგენს navbar - სანავიგაციო ზოლი.
Bootstrap-ის კლასი შეგვიძლია დავუმატოთ <nav> ელემენტს სტილისა და ფუნქციონალის განსასაზღვრად.
ბუტსტრეპის ნავბარები არის რესპონსივ ელემენტები რაც ნიშნავს რომ ის ავტომატურად იცვლის ზომას ან ფორმას
ეკრანის ტიპისა და გაფართოების გათვალისწინებით.

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
      <a class="nav-link" href="#">Features</a>
      <a class="nav-link" href="#">Pricing</a>
      <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
    </div>
  </div>
</nav>
```
