rm -rf build
rm -rf dist

cd vgem
rm -rf vgem.egg-info

cd ..

python3 setup.py sdist bdist_wheel