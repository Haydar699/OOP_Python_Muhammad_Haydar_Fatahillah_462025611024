
# SISTEM ADMINISTRASI RUMAH SAKIT YASYFIN
# Final Project Object-Oriented Programming



# CUSTOM EXCEPTIONS

class HospitalError(Exception):
    """Base exception untuk sistem rumah sakit."""
    pass


class PatientNotFoundError(HospitalError):
    """Terjadi ketika pasien tidak ditemukan."""
    pass


class DoctorNotFoundError(HospitalError):
    """Terjadi ketika dokter tidak ditemukan."""
    pass


class InvalidDataError(HospitalError):
    """Terjadi ketika data yang dimasukkan tidak valid."""
    pass


# CLASS PERSON
# Parent / Superclass

class Person:

    def __init__(self, person_id, name, phone):
        self.__person_id = person_id
        self.__name = name
        self.__phone = phone

    # Getter
    def get_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    # Setter
    def set_name(self, name):
        if not name.strip():
            raise InvalidDataError("Nama tidak boleh kosong.")

        self.__name = name

    def set_phone(self, phone):
        if not self.validate_phone(phone):
            raise InvalidDataError("Nomor telepon tidak valid.")

        self.__phone = phone

    # Static Method
    @staticmethod
    def validate_phone(phone):
        """Memvalidasi nomor telepon."""
        return phone.isdigit() and len(phone) >= 10

    # Magic Method
    def __str__(self):
        return f"{self.__person_id} - {self.__name} - {self.__phone}"


# CLASS PATIENT
# Subclass dari Person

class Patient(Person):

    def __init__(self, patient_id, name, phone, address):
        super().__init__(patient_id, name, phone)

        self.__address = address

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    # Method ini akan di-override oleh subclass
    # Inilah bagian utama POLYMORPHISM
    def calculate_bill(self, treatment_cost):
        return treatment_cost

    def __str__(self):
        return (
            f"ID: {self.get_id()} | "
            f"Nama: {self.get_name()} | "
            f"Telepon: {self.get_phone()} | "
            f"Alamat: {self.__address}"
        )


# ============================================================
# CLASS GENERAL PATIENT
# Subclass dari Patient
# ============================================================

class GeneralPatient(Patient):

    def calculate_bill(self, treatment_cost):
        # Pasien umum membayar biaya penuh
        return treatment_cost

    def __str__(self):
        return f"[Pasien Umum] {super().__str__()}"


# ============================================================
# CLASS INSURANCE PATIENT
# Subclass dari Patient
# ============================================================

class InsurancePatient(Patient):

    def __init__(
        self,
        patient_id,
        name,
        phone,
        address,
        insurance_coverage
    ):
        super().__init__(patient_id, name, phone, address)

        self.__insurance_coverage = insurance_coverage

    def get_insurance_coverage(self):
        return self.__insurance_coverage

    def calculate_bill(self, treatment_cost):
        # Menghitung biaya yang harus dibayar pasien
        coverage = treatment_cost * (
            self.__insurance_coverage / 100
        )

        return treatment_cost - coverage

    def __str__(self):
        return (
            f"[Pasien Asuransi] {super().__str__()} | "
            f"Tanggungan Asuransi: {self.__insurance_coverage}%"
        )


# ============================================================
# CLASS DOCTOR
# Subclass dari Person
# ============================================================

class Doctor(Person):

    def __init__(
        self,
        doctor_id,
        name,
        phone,
        specialization
    ):
        super().__init__(doctor_id, name, phone)

        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def __str__(self):
        return (
            f"ID: {self.get_id()} | "
            f"Dr. {self.get_name()} | "
            f"Spesialis: {self.__specialization} | "
            f"Telepon: {self.get_phone()}"
        )


# ============================================================
# CLAS ADMIN
# Subclass dari Person 
# ============================================================

class Admin(Person):

    def __init__(
        self,
        admin_id,
        name,
        phone,
        username
    ):
        super().__init__(admin_id, name, phone)

        self.__username = username

    def get_username(self):
        return self.__username

    def __str__(self):
        return (
            f"ID: {self.get_id()} | "
            f"Admin: {self.get_name()} | "
            f"Username: {self.__username}"
        )


# ============================================================
# CLASS MEDICAL RECORD
# ============================================================

class MedicalRecord:

    def __init__(
        self,
        record_id,
        patient,
        doctor,
        diagnosis,
        treatment
    ):
        self.__record_id = record_id
        self.__patient = patient
        self.__doctor = doctor
        self.__diagnosis = diagnosis
        self.__treatment = treatment

    def get_patient(self):
        return self.__patient

    def get_doctor(self):
        return self.__doctor

    def __str__(self):
        return (
            f"Record ID: {self.__record_id}\n"
            f"Pasien: {self.__patient.get_name()}\n"
            f"Dokter: {self.__doctor.get_name()}\n"
            f"Diagnosis: {self.__diagnosis}\n"
            f"Tindakan: {self.__treatment}"
        )


# ============================================================
# CLASS SCHEDULE
# ============================================================

class Schedule:

    def __init__(
        self,
        schedule_id,
        doctor,
        day,
        time
    ):
        self.__schedule_id = schedule_id
        self.__doctor = doctor
        self.__day = day
        self.__time = time

    def __str__(self):
        return (
            f"Jadwal {self.__schedule_id} | "
            f"Dr. {self.__doctor.get_name()} | "
            f"{self.__day}, {self.__time}"
        )


# ============================================================
# CLASS PAYMENT
# ============================================================

class Payment:

    def __init__(
        self,
        payment_id,
        patient,
        treatment_cost
    ):
        self.__payment_id = payment_id
        self.__patient = patient
        self.__treatment_cost = treatment_cost

        # POLYMORPHISM
        # Kita tidak perlu tahu pasiennya tipe apa.
        # Cukup panggil calculate_bill().
        self.__total = patient.calculate_bill(treatment_cost)

    def get_total(self):
        return self.__total

    def __str__(self):
        return (
            f"Payment ID: {self.__payment_id}\n"
            f"Pasien: {self.__patient.get_name()}\n"
            f"Biaya Awal: Rp{self.__treatment_cost:,.0f}\n"
            f"Total Bayar: Rp{self.__total:,.0f}"
        )


# ============================================================
# CLASS HOSPITAL
# Class utama
# ============================================================

class Hospital:

    def __init__(self, name):
        self.__name = name

        self.__patients = []
        self.__doctors = []
        self.__admins = []
        self.__medical_records = []
        self.__schedules = []
        self.__payments = []

    # --------------------------------------------------------
    # PATIENT
    # --------------------------------------------------------

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_patient(self, patient_id):

        for patient in self.__patients:

            if patient.get_id() == patient_id:
                return patient

        raise PatientNotFoundError(
            f"Pasien dengan ID {patient_id} tidak ditemukan."
        )

    def show_patients(self):

        if not self.__patients:
            print("\nBelum ada data pasien.")
            return

        print("\n========== DAFTAR PASIEN ==========")

        for patient in self.__patients:
            print(patient)

    # --------------------------------------------------------
    # DOCTOR
    # --------------------------------------------------------

    def add_doctor(self, doctor):
        self.__doctors.append(doctor)

    def get_doctor(self, doctor_id):

        for doctor in self.__doctors:

            if doctor.get_id() == doctor_id:
                return doctor

        raise DoctorNotFoundError(
            f"Dokter dengan ID {doctor_id} tidak ditemukan."
        )

    def show_doctors(self):

        if not self.__doctors:
            print("\nBelum ada data dokter.")
            return

        print("\n========== DAFTAR DOKTER ==========")

        for doctor in self.__doctors:
            print(doctor)

    # --------------------------------------------------------
    # MEDICAL RECORD
    # --------------------------------------------------------

    def add_medical_record(self, record):
        self.__medical_records.append(record)

    def show_medical_records(self):

        if not self.__medical_records:
            print("\nBelum ada rekam medis.")
            return

        print("\n========== REKAM MEDIS ==========")

        for record in self.__medical_records:
            print(record)
            print("----------------------------------")

    # --------------------------------------------------------
    # SCHEDULE
    # --------------------------------------------------------

    def add_schedule(self, schedule):
        self.__schedules.append(schedule)

    def show_schedules(self):

        if not self.__schedules:
            print("\nBelum ada jadwal.")
            return

        print("\n========== JADWAL DOKTER ==========")

        for schedule in self.__schedules:
            print(schedule)

    # --------------------------------------------------------
    # PAYMENT
    # --------------------------------------------------------

    def add_payment(self, payment):
        self.__payments.append(payment)

    def show_payments(self):

        if not self.__payments:
            print("\nBelum ada pembayaran.")
            return

        print("\n========== DATA PEMBAYARAN ==========")

        for payment in self.__payments:
            print(payment)
            print("-------------------------------------")

    # --------------------------------------------------------
    # HOSPITAL INFORMATION
    # --------------------------------------------------------

    def show_info(self):

        print("\n======================================")
        print(f"   SISTEM ADMINISTRASI {self.__name.upper()}")
        print("======================================")
        print(f"Jumlah Pasien : {len(self.__patients)}")
        print(f"Jumlah Dokter : {len(self.__doctors)}")
        print(
            f"Jumlah Rekam Medis : "
            f"{len(self.__medical_records)}"
        )
        print(
            f"Jumlah Pembayaran : "
            f"{len(self.__payments)}"
        )


# ============================================================
# FUNGSI INPUT PASIEN
# ============================================================

def add_patient_menu(hospital):

    try:

        print("\n========== TAMBAH PASIEN ==========")

        patient_id = input("ID Pasien       : ")
        name = input("Nama            : ")
        phone = input("No. Telepon     : ")
        address = input("Alamat          : ")

        if not Person.validate_phone(phone):
            raise InvalidDataError(
                "Nomor telepon harus berupa angka "
                "dan minimal 10 digit."
            )

        print("\nJenis Pasien:")
        print("1. Pasien Umum")
        print("2. Pasien Asuransi")

        patient_type = input("Pilih: ")

        if patient_type == "1":

            patient = GeneralPatient(
                patient_id,
                name,
                phone,
                address
            )

        elif patient_type == "2":

            coverage = float(
                input("Persentase tanggungan asuransi: ")
            )

            if coverage < 0 or coverage > 100:
                raise InvalidDataError(
                    "Persentase harus antara 0-100."
                )

            patient = InsurancePatient(
                patient_id,
                name,
                phone,
                address,
                coverage
            )

        else:

            raise InvalidDataError(
                "Jenis pasien tidak valid."
            )

        hospital.add_patient(patient)

        print("\nPasien berhasil ditambahkan.")

    except ValueError:

        print(
            "\nError: Masukkan angka yang valid."
        )

    except HospitalError as error:

        print(f"\nError: {error}")


# ============================================================
# FUNGSI INPUT DOKTER
# ============================================================

def add_doctor_menu(hospital):

    try:

        print("\n========== TAMBAH DOKTER ==========")

        doctor_id = input("ID Dokter       : ")
        name = input("Nama             : ")
        phone = input("No. Telepon      : ")
        specialization = input("Spesialisasi     : ")

        if not Person.validate_phone(phone):
            raise InvalidDataError(
                "Nomor telepon tidak valid."
            )

        doctor = Doctor(
            doctor_id,
            name,
            phone,
            specialization
        )

        hospital.add_doctor(doctor)

        print("\nDokter berhasil ditambahkan.")

    except HospitalError as error:

        print(f"\nError: {error}")


# ============================================================
# FUNGSI INPUT REKAM MEDIS
# ============================================================

def add_medical_record_menu(hospital):

    try:

        print("\n========== TAMBAH REKAM MEDIS ==========")

        record_id = input("ID Rekam Medis : ")
        patient_id = input("ID Pasien      : ")
        doctor_id = input("ID Dokter      : ")

        patient = hospital.get_patient(patient_id)
        doctor = hospital.get_doctor(doctor_id)

        diagnosis = input("Diagnosis      : ")
        treatment = input("Tindakan       : ")

        record = MedicalRecord(
            record_id,
            patient,
            doctor,
            diagnosis,
            treatment
        )

        hospital.add_medical_record(record)

        print("\nRekam medis berhasil ditambahkan.")

    except HospitalError as error:

        print(f"\nError: {error}")


# ============================================================
# FUNGSI INPUT JADWAL
# ============================================================

def add_schedule_menu(hospital):

    try:

        print("\n========== TAMBAH JADWAL ==========")

        schedule_id = input("ID Jadwal      : ")
        doctor_id = input("ID Dokter      : ")

        doctor = hospital.get_doctor(doctor_id)

        day = input("Hari           : ")
        time = input("Jam            : ")

        schedule = Schedule(
            schedule_id,
            doctor,
            day,
            time
        )

        hospital.add_schedule(schedule)

        print("\nJadwal berhasil ditambahkan.")

    except HospitalError as error:

        print(f"\nError: {error}")


# ============================================================
# FUNGSI PEMBAYARAN
# ============================================================

def payment_menu(hospital):

    try:

        print("\n========== PEMBAYARAN ==========")

        payment_id = input("ID Pembayaran : ")
        patient_id = input("ID Pasien     : ")

        patient = hospital.get_patient(patient_id)

        treatment_cost = float(
            input("Biaya Pengobatan : Rp")
        )

        if treatment_cost < 0:
            raise InvalidDataError(
                "Biaya tidak boleh negatif."
            )

        payment = Payment(
            payment_id,
            patient,
            treatment_cost
        )

        hospital.add_payment(payment)

        print("\nPembayaran berhasil.")
        print(
            f"Total yang harus dibayar: "
            f"Rp{payment.get_total():,.0f}"
        )

    except ValueError:

        print(
            "\nError: Masukkan nominal berupa angka."
        )

    except HospitalError as error:

        print(f"\nError: {error}")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    hospital = Hospital(
        "Rumah Sakit Yasyfin"
    )

    while True:

        print("\n")
        print("==========================================")
        print("     SISTEM ADMINISTRASI RS YASYFIN")
        print("==========================================")
        print("1. Tambah Pasien")
        print("2. Lihat Daftar Pasien")
        print("3. Tambah Dokter")
        print("4. Lihat Daftar Dokter")
        print("5. Tambah Rekam Medis")
        print("6. Lihat Rekam Medis")
        print("7. Tambah Jadwal Dokter")
        print("8. Lihat Jadwal Dokter")
        print("9. Pembayaran")
        print("10. Lihat Pembayaran")
        print("11. Informasi Rumah Sakit")
        print("0. Keluar")
        print("==========================================")

        choice = input("Pilih menu: ")

        if choice == "1":

            add_patient_menu(hospital)

        elif choice == "2":

            hospital.show_patients()

        elif choice == "3":

            add_doctor_menu(hospital)

        elif choice == "4":

            hospital.show_doctors()

        elif choice == "5":

            add_medical_record_menu(hospital)

        elif choice == "6":

            hospital.show_medical_records()

        elif choice == "7":

            add_schedule_menu(hospital)

        elif choice == "8":

            hospital.show_schedules()

        elif choice == "9":

            payment_menu(hospital)

        elif choice == "10":

            hospital.show_payments()

        elif choice == "11":

            hospital.show_info()

        elif choice == "0":

            print("\nTerima kasih telah menggunakan")
            print("Sistem Administrasi Rumah Sakit Yasyfin.")
            break

        else:

            print(
                "\nPilihan tidak valid. "
                "Silakan coba lagi."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()