# homeassistant-custom-components-pagerduty
Adds a Catholic Calendar sensor to home assistant.

Based off of https://github.com/Liturgical-Calendar/LiturgicalCalendarAPI for determining calendar logic
Credit to @JohnRDOrazio

## Support
[![coffee](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](https://www.buymeacoffee.com/jmacri)

## Getting Started

### Install component
Add as a custom HACS repository
OR
Copy `/custom_components/catholic_calendar/` to the following directory in Home Assistant:
`<config directory>/custom_components/catholic_calendar/`

### Define sensor
Add the following to `<config directory>/configuration.yaml`
**Example configuration.yaml:**

```yaml
sensor:
  - platform: catholic_calendar
    name: Catholic Calendar
```

**Configuration variables:**

key | description
:--- | :---
**platform (Required)** | The platform name
**name (Required)** | Name your feed
***