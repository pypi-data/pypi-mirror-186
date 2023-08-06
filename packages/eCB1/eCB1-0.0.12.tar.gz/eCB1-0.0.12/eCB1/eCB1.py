from requests.auth import HTTPBasicAuth
import requests
import json


class eCB1:
    def __init__(self, username, password, url, requestGetTimeOut = None):
        self.username = username
        self.password = password
        self.baseUrl = url
        self._requestGetTimeout = requestGetTimeOut
        self.jwtToken = ""
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json;charset=UTF-8",
        }

    @property
    def requestGetTimeOut(self):
        return self._requestGetTimeout

    def authenticate(self):
        # untested authentication with eCB1 thus, this
        # function will always return true for now
        return bool(1)
        try:
            response = requests.get(
                f"{self.baseUrl}",
                auth=HTTPBasicAuth(self.username, self.password),
                timeout=self._requestGetTimeout
            )
        except requests.exceptions.HTTPError as err:
            raise (err)
        self.jwtToken = json.loads(response.text)
        self.headers["Authorization"] = f"Bearer {self.jwtToken}"

    def getChargersList(self):
        chargerIds = []
        try:
            response = requests.get(
                f"{self.baseUrl}api/v1/chargecontrols", headers = self.headers,
                timeout=self._requestGetTimeout
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
                raise (err)
        for group in json.loads(response.text)["chargecontrols"]:
            chargerIds.append(group["id"])
        return chargerIds

    def getChargerStatus(self, chargerId):
        try:
            response = requests.get(
                f"{self.baseUrl}api/v1/chargecontrols/{chargerId}", headers = self.headers,
                timeout=self._requestGetTimeout
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
                raise(err)
        return json.loads(response.text)

    def unlockCharger(self, chargerId):
        try:
            response = requests.get(
                f"{self.baseUrl}?charge=start:{chargerId}", headers=self.headers,
                timeout=self._requestGetTimeout
            )
            #response.raise_for_status()
        except requests.exceptions.HTTPError as err:
                raise(err)
        return response.status_code == requests.codes.ok

    def lockCharger(self, chargerId):
        try:
            response = requests.get(
                f"{self.baseUrl}?charge=stop:{chargerId}", headers=self.headers,
                timeout=self._requestGetTimeout
            )
            #response.raise_for_status()
        except requests.exceptions.HTTPError as err:
                raise(err)
        return response.status_code == requests.codes.ok

    def setMaxChargingCurrent(self, chargerId, newMaxChargingCurrentValue):

        if self.getAbsoluteMaxChargingCurrent(chargerId) <= newMaxChargingCurrentValue:
            newMaxChargingCurrentValue = self.getAbsoluteMaxChargingCurrent(chargerId)
        try:
            response = requests.post(
                f"{self.baseUrl}api/v1/chargecontrols/{chargerId}/mode/manual/ampere", headers=self.headers,
                timeout=self._requestGetTimeout,
                data=f"manualmodeamp={newMaxChargingCurrentValue}",
            )
        except requests.exceptions.HTTPError as err:
                raise(err)

        return response.status_code == requests.codes.ok

    def getAbsoluteMaxChargingCurrent(self, chargerId):
        """Not yet implemented, thus just returns 32A"""
        return 32

    def getSystemInformation(self):
        """Loads System Information, such as serials, etc"""
        try:
            response = requests.get(
                f"{self.baseUrl}api/v1/all", headers=self.headers,
                timeout=self._requestGetTimeout
            )
        except requests.exceptions.HTTPError as err:
            raise(err)
        return json.loads(response.text)['system']

    def getChargingModes(self):
        """Hardy Barth eCB1 does not provide list of modes, thus, its a static return"""
        modes = '{"1": "eco", "2":"quick", "3":"manual"}'
        return json.loads(modes)

    def setChargingMode(self, chargerId, mode):
        """Sets the charging mode (eco, manual, quick)"""
        try:
            response = requests.post(
                f"{self.baseUrl}api/v1/chargecontrols/{chargerId}/mode/",
                headers=self.headers,
                timeout=self._requestGetTimeout,
                data=f"mode={mode}",
            )
        except requests.exceptions.HTTPError as err:
            raise(err)

    def getAutoStartStopMode(self, chargerId):
        """Loads the status of the AutoStartStop Mode
        (eCharge Hardy Barth calls this AI Mode) = Surplus Charging"""
        try:
            response = requests.get(
                f"{self.baseUrl}api/v1/chargecontrols/{chargerId}/mode/eco/startstop",
                headers=self.headers,
                timeout=self._requestGetTimeout
            )
        except requests.exceptions.HTTPError as err:
            raise(err)
        return json.loads(response.text)

    def setAutoStartStopMode(self, chargerId, onOrOff):
        """sets the status of the AutoStartStop Mode
        (eCharge Hardy Barth calls this AI Mode) = Surplus Charging"""
        """onOrOff = true -> enable AI Mode"""
        try:
            response = requests.post(
                f"{self.baseUrl}api/v1/chargecontrols/{chargerId}/mode/eco/startstop",
                headers=self.headers,
                timeout=self._requestGetTimeout,
                data=f"autostartstop={onOrOff}",
            )
        except requests.exceptions.HTTPError as err:
            raise(err)

    def getMetersData(self, chargerId):
        """loads the meters data for the Wallbox"""
        try:
            response = requests.get(
                f"{self.baseUrl}api/v1/meters/{chargerId}",
                headers=self.headers,
                timeout=self._requestGetTimeout,
            )
        except requests.exceptions.HTTPError as err:
            raise(err)
        return json.loads(response.text)
