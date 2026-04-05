cat > setup.py << 'EOF'
from setuptools import setup

setup(
    name="myserverlib",
    version="0.1.0",
    py_modules=["myserverlib"],
)
EOF
