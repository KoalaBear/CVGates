# CVGates

## Shared Parking Lot Management, Made Easy.

You can **NOW** Get rid of all your remotes & switches, AND Easily move to a smart gate operating method, with the ability to limit the amount of vehicles per resident in your parking, all with a
10-minute setup!


<!-- TABLE OF CONTENTS -->

## Table of Contents

* [About the Project](#about-the-project)
    * [Built With](#built-with)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

CVGates lets you easily replace your manually controlled gate with an automated CV Plate Number recognition based switch.
by thus, allowing you to also easily permit residents to a specific amount of vehicles, which they can even update by themselves once you assign their user a permit to enter a Plate Number which would be able to open the parking gate.

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
3. Set your `frame grabbing` logic on `camera/grab_frame.py`
4. Create a super user by passing `createsuperuser` as a parameter to `main.py`
5. Create a user for all your residents at `YOUR_URL/admin/` and then... Enjoy your use!

<!-- USAGE EXAMPLES -->

## Usage

Screenshots would be added here =]

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/KoalaBear/CVGates/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

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

[contributors-url]: https://github.com/KoalaBear/CVGates/graphs/contributors

[forks-url]: https://github.com/KoalaBear/CVGates/network/members

[stars-url]: https://github.com/KoalaBear/CVGates/stargazers

[issues-url]: https://github.com/KoalaBear/CVGates/issues

[license-url]: https://github.com/KoalaBear/CVGates/blob/master/LICENSE.txt

[product-screenshot]: resources/images/screenshot.png
