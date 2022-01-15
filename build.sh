rm -rf build
rm -rf dist

cd src
rm -rf vg_em.egg-info

cd ..

python3 setup.py sdist bdist_wheel