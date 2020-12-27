
# CVGates 
## Shared Parking Lot Management, Made Easy.
**You can now** Get rid of manual switches or remotes AND Easily limit the amount of vehicles per resident, all with a 10-minute setup!




<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project
CVGates lets you easily replace your manually controlled gate with an automated CV Plate Number recognition- switch.
by thus, allowing you to easily limit all residents by a specific amount of digital permits- which can be assigned by them to their very own plate numbers.


### Built With

* [Django]()
* [Bootstrap 5 Base-Dashboard](https://github.com/themesberg/volt-bootstrap-5-dashboard)
* [Tesseract](https://github.com/tesseract-ocr/tesseract)
* [OpenCV](https://github.com/opencv/opencv)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
* pip
```sh
pip install -r requirements.txt
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/KoalaBear/CVGates.git
```
2. Set your `gate toggling` logic on `gate_controls/toggle.py`'s functions
3. Set your `frame taking` logic on `realtime_recognition.py`
4. Create a super user by passing `createsuperuser` as a parameter to `main.py`
5. Create a user for all your residents at `YOUR_URL/admin/` and.. Enjoy it all!



<!-- USAGE EXAMPLES -->
## Usage

Screenshots would be added here =]

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/KoalaBear/CVGates/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPL V3 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact
[KoalaBear's Mail](mailto:koalabeardevelopments@gmail.com)
KoalaBear @ GitHub
Project's Link: [https://github.com/KoalaBear/CVGates](https://github.com/KoalaBear/CVGates)

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/KoalaBear/CVGates/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/KoalaBear/CVGates/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/KoalaBear/CVGates/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/KoalaBear/CVGates/issues
[license-shield]: https://img.shields.io/github/license/KoalaBear/repo.svg?style=flat-square
[license-url]: https://github.com/KoalaBear/CVGates/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/KoalaBear
[product-screenshot]: resources/images/screenshot.png
