SUBJECT_LIST = [
    "Complexity Theory",
    "Advanced Algorithms",
    #"Advanced Architecture and OS",
    "Deep Learning",
    "Computer Graphics",
    "Natural Language Understanding",
    "Machine Learning with Big Data",
    "Computer Vision",
    "Advanced Machine Learning",
    "Speech Understanding",
    #"ML-Ops and DL-Ops",
    "Introduction to Blockchain",
    "Virtualization and Cloud Computing"
]


DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

SLOTS = [
    "08:00 - 08:50",
    "09:00 - 09:50",
    "10:00 - 10:50",
    "11:00 - 11:50",
    "12:00 - 12:50",
    "01:00 - 01:50",  # Lunch / Break
    "02:00 - 02:50",
    "03:00 - 03:50",
    "04:00 - 04:50",
    "05:00 - 05:50",
    "06:00 - 07:30"
]

TIMETABLE = {
    "Monday": {
        "02:00 - 02:50": {
            "subject": "Advanced Architecture and OS",
            "faculty": "Palash Das",
            "venue": ""
        },
        "03:00 - 03:50": {
            "subject": "Computer Graphics",
            "faculty": "Hardik Jain",
            "venue": ""
        },
        "04:00 - 04:50": {
            "subject": "Computer Vision",
            "faculty": "Deepak Mishra",
            "venue": ""
        },
        "06:00 - 07:30": {
            "subject": "Speech Understanding",
            "faculty": "Richa Singh",
            "venue": ""
        }
    },

    "Tuesday": {
        "08:00 - 08:50": {
            "subject": "Introduction to Blockchain",
            "faculty": "Susil Kumar Mohanty",
            "venue": ""
        },
        "11:00 - 11:50": {
            "subject": "Complexity Theory",
            "faculty": "Vimal Raj Sharma",
            "venue": "LHC 2 102"
        },
        "02:00 - 02:50": {
            "subject": "Advanced Architecture and OS",
            "faculty": "Palash Das",
            "venue": ""
        },
        "03:00 - 03:50": {
            "subject": "Deep Learning",
            "faculty": "Angshuman Paul",
            "venue": "LHC 1 308"
        },
        "06:00 - 07:30": {   # ✅ UPDATED NLU
            "subject": "Natural Language Understanding",
            "faculty": "Anand Mishra",
            "venue": "LHC 1 308"
        }
    },

    "Wednesday": {
        "02:00 - 02:50": {
            "subject": "Deep Learning",
            "faculty": "Angshuman Paul",
            "venue": "LHC 1 308"
        },
        "03:00 - 03:50": {
            "subject": "Computer Graphics",
            "faculty": "Hardik Jain",
            "venue": ""
        },
        "04:00 - 04:50": {
            "subject": "Computer Vision",
            "faculty": "Deepak Mishra",
            "venue": "LHC 1 308"
        },
        "05:00 - 05:50": {
            "subject": "Ethics",
            "faculty": "—",
            "venue": ""
        },
        "06:00 - 07:30": {
            "subject": "Virtualization and Cloud Computing",
            "faculty": "Sumit Kalra",
            "venue": ""
        }
    },

    "Thursday": {
        "08:00 - 08:50": {
            "subject": "Introduction to Blockchain",
            "faculty": "Susil Kumar Mohanty",
            "venue": ""
        },
        "11:00 - 11:50": {
            "subject": "Complexity Theory",
            "faculty": "Vimal Raj Sharma",
            "venue": "LHC 2 102"
        },
        "02:00 - 02:50": {
            "subject": "Advanced Architecture and OS",
            "faculty": "Palash Das",
            "venue": ""
        },
        "03:00 - 03:50": {
            "subject": "Computer Graphics",
            "faculty": "Hardik Jain",
            "venue": ""
        }
    },

    "Friday": {
        "11:00 - 11:50": {
            "subject": "Complexity Theory",
            "faculty": "Vimal Raj Sharma",
            "venue": "LHC 2 102"
        },
        "02:00 - 02:50": {
            "subject": "Deep Learning",
            "faculty": "Angshuman Paul",
            "venue": "LHC 1 308"
        },
        "03:00 - 03:50": {
            "subject": "Computer Vision",
            "faculty": "Deepak Mishra",
            "venue": "LHC 1 308"
        },
        "05:00 - 05:50": {
            "subject": "Introduction to Blockchain",
            "faculty": "Susil Kumar Mohanty",
            "venue": ""
        }
    },

    "Saturday": {
        "02:00 - 02:50": {   # ✅ UPDATED NLU
            "subject": "Natural Language Understanding",
            "faculty": "Anand Mishra",
            "venue": "LHC 1 308"
        },
        "03:00 - 03:50": {
            "subject": "Virtualization and Cloud Computing",
            "faculty": "Sumit Kalra",
            "venue": ""
        },
        "06:00 - 07:30": {
            "subject": "Machine Learning with Big Data",
            "faculty": "Dip Sankar Banerjee",
            "venue": ""
        }
    }
}